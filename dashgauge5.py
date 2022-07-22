#GAUGE WITH MCP3008

import dash_daq as daq
import dash_bootstrap_components as dbc
import js2py
from dash import Dash, dash, dcc, html
from dash.dependencies import Input, Output
import os
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

freshINPUT = 0
grayINPUT = 0
blackINPUT = 0

# create the spi bus
SPI = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# create the cs (chip select)
chipSelect = digitalio.DigitalInOut(board.D5)
# create the mcp object
mcpObject = MCP.MCP3008(SPI, chipSelect)
# create an analog input channel on pin 0
channel1 = AnalogIn(mcpObject, MCP.P0)
channel2 = AnalogIn(mcpObject, MCP.P1)
channel3 = AnalogIn(mcpObject, MCP.P3)

def getFresh():
    id='freshInput'
    return GPIO.input(freshINPUT)
def getGray():
    id='grayInput'
    return GPIO.input(grayINPUT)
def getBlack():
    id='blackInput'
    return GPIO.input(blackINPUT)


print('Raw ADC Value: ', channel.value)
print('ADC Voltage: ' + str(channel.voltage) + 'V')

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
