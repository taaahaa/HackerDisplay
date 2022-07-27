#GAUGE WITH RASPI/ARDUINO INPUT

import dash_daq as daq
import dash_bootstrap_components as dbc
import js2py
from dash import Dash, dash, dcc, html
from dash.dependencies import Input, Output
import RPi.GPIO as GPIO
import serial
import os

freshINPUT = 0
grayINPUT = 0
blackINPUT = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(freshINPUT, GPIO.IN)
GPIO.setup(grayINPUT, GPIO.IN)
GPIO.setup(blackINPUT, GPIO.IN)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

def getFresh():
    water = ser.read()
    if water == "freshInput" and ser <=100 and ser >=0:
        freshInput = ser.read()
        return freshInput

def getGray():
    water = ser.read()
    if water == "grayInput" and ser <=100 and ser >=0:
        grayInput = ser.read()
        return grayInput
def getBlack():
    water = ser.read()
    if water == "blackInput" and ser <=100 and ser >=0:
        blackInput = ser.read()
        return blackInput

app = dash.Dash(__name__,assets_url_path='/assets/gauge.css',
                external_stylesheets=[dbc.themes.DARKLY],
                suppress_callback_exceptions = True)

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div(children=[
    html.Div([
        html.Div([
            daq.Gauge(
                label='FRESH',
                labelPosition='bottom',
                id='fresh',
                value=getFresh(),
                max=100,
                min=0,
                color={
                    "gradient": True,
                    "ranges": {
                        "red": [0, 25],
                        "orange":[25, 50],
                        "yellow":[50, 75],
                        "green":[75, 100]
                    }
                },
                scale={
                    'start': 0,
                    'interval': 25,
                    'labelInterval': 1,
                }
            ), 
            dcc.Input(
                id='freshInput',
                type='hidden',
                autoComplete='True',
                value=getFresh(),
            )
        ], className='four columns'),

        html.Div([
            daq.Gauge(
                label='GRAY',
                labelPosition='bottom',
                id='gray',
                value=getGray(),
                max=100,
                min=0,
                color={
                    "gradient": True,
                    "ranges": {
                        "red": [0, 25],
                        "orange":[25, 50],
                        "yellow":[50, 75],
                        "green":[75, 100]}
                },
                scale={
                    'start': 0,
                    'interval': 25,
                    'labelInterval': 1,
                },
            ),
            dcc.Input(
                id='grayInput',
                type='hidden',
                autoComplete='True',
                value=getGray(),
            )
        ], className='four columns'),

        html.Div([
            daq.Gauge(
                label='BLACK',
                labelPosition='bottom',
                id='black',
                value=getBlack(),
                max=100,
                min=0,
                color={
                    "gradient": True,
                    "ranges": {
                        "red": [0, 25],
                        "orange":[25, 50],
                        "yellow":[50, 75],
                        "green":[75, 100]
                    }
                },
                scale={
                    'start': 0,
                    'interval': 25,
                    'labelInterval': 1,
                }
            ),
            dcc.Input(
                id='blackInput',
                type='hidden',
                autoComplete='True',
                value= getBlack(),
            )
        ], className='four columns'),
    ], className='row', style={'text-align': 'center', 'verticalAlign': 'middle', 'display': 'inline'}),
])

@app.callback(Output(component_id='fresh', component_property='value'),
              Output(component_id='gray', component_property='value'),
              Output(component_id='black', component_property='value'),
              Input(component_id='freshInput', component_property='value'),
              Input(component_id='grayInput', component_property='value'),
              Input(component_id='blackInput', component_property='value'),
              )

def update_output(freshInput, grayInput, blackInput):
    return getFresh(), getGray(), getBlack()


if __name__ == '__main__':
    app.run_server(debug=True)
    