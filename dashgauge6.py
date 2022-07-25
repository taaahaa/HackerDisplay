#GAUGE WITH ADS7830

import dash_daq as daq
import dash_bootstrap_components as dbc
import js2py
from dash import Dash, dash, dcc, html
from dash.dependencies import Input, Output
from smbus import SMBus
import os

freshINPUT = 18
grayINPUT = 0
blackINPUT = 0

def getFresh():
    id='freshInput'
    return bus.read_byte(0x4b)
def getGray():
    id='grayInput'
    return GPIO.input(grayINPUT)
def getBlack():
    id='blackInput'
    return GPIO.input(blackINPUT)

app = dash.Dash(__name__,assets_url_path='/assets/gauge.css',external_stylesheets=[dbc.themes.DARKLY])

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div(children=[
    html.Div([
        html.Div([
            daq.Gauge(
                label='FRESH',
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
        ], className='four columns'),

        html.Div([
            daq.Gauge(
                label='GRAY',
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
        ], className='four columns'),

        html.Div([
            daq.Gauge(
                label='BLACK',
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
        ], className='four columns'),
    ], className='row', style={'text-align': 'center', 'verticalAlign': 'middle', 'display': 'inline'}),
])

@app.callback(Output(component_id='fresh', component_property='value'),
              Output(component_id='gray', component_property='value'),
              Output(component_id='black', component_property='value'),
              )

def update_output(freshInput, grayInput, blackInput):
    return getFresh(), getGray(), getBlack()


if __name__ == '__main__':
    app.run_server(debug=True)
