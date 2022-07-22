#TESTING I/O FOR MCP3008

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time


# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# create the cs (chip select)
chipSelect = digitalio.DigitalInOut(board.D5)
# create the mcp object
mcpObject = MCP.MCP3008(spi, chipSelect)
# create an analog input channel on pin 0
channel = AnalogIn(mcpObject, MCP.P0)

while (True):
    print('Raw ADC Value: ', channel.value)
    print('ADC Voltage: ' + str(channel.voltage) + 'V')
    time.sleep(1)
    