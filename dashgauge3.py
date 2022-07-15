#GAUGE WITH LOCAL FILES

from cProfile import label
import dash_daq as daq
import dash_bootstrap_components as dbc
import js2py
from dash import Dash, dash, dcc, html
from dash.dependencies import Input, Output
import os

# assets_url_path='/assets/gauge.css'

app = dash.Dash(__name__,include_assets_files=True,external_stylesheets=[dbc.themes.DARKLY])

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div(children=[
    html.Div([
        html.Div([
            daq.Gauge(
                label='FRESH',
                labelPosition='bottom',
                id='fresh',
                value=0,
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
            dcc.Slider(
                id='slider1',
                min=0,
                max=100,
                step=5,
                value=0,
            )
        ], className='four columns'),

        html.Div([
            daq.Gauge(
                label='GRAY',
                labelPosition='bottom',
                id='gray',
                value=0,
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
            dcc.Slider(
                id='slider2',
                min=0,
                max=100,
                step=5,
                value=0,
            ),
        ], className='four columns'),

        html.Div([
            daq.Gauge(
                label='BLACK',
                labelPosition='bottom',
                id='black',
                value=0,
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
            dcc.Slider(
                id='slider3',
                min=0,
                max=100,
                step=5,
                value=0,
            )
        ], className='four columns'),
    ], className='row', style={}),
])

@app.callback(Output(component_id='fresh', component_property='value'),
              Output(component_id='gray', component_property='value'),
              Output(component_id='black', component_property='value'),
              Input(component_id='slider1', component_property='value'),
              Input(component_id='slider2', component_property='value'),
              Input(component_id='slider3', component_property='value'),
              )

def update_output(slider1, slider2, slider3):
    return slider1, slider2, slider3


if __name__ == '__main__':
    app.run_server(debug=True)