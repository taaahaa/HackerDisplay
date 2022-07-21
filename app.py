#MAIN CODE

from re import U
import dash_daq as daq
import dash_bootstrap_components as dbc
import js2py
from dash import Dash, dash, dcc, html
from dash.dependencies import Input, Output
import RPi.GPIO as GPIO
import os

import callbacks, layout

app = Dash(__name__,assets_url_path='/assets/gauge.css',external_stylesheets=[dbc.themes.DARKLY])
