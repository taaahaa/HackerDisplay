from time import sleep
from gpiozero import MCP3008

gaugeIn = MCP3008(0)

while True:
    print("Raw output: " + gaugeIn.value)   
    print("not-Raw output: " + int(gaugeIn.value))   
    time.sleep(1)