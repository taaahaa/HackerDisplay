from re import T
from gpiozero import MCP3008

gaugeIn = MCP3008(0)

while True:
    print(gaugeIn.value)   