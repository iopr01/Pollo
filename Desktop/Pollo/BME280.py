# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
from adafruit_bme280 import basic as adafruit_bme280
#from simple_pid import PID

def funcion1():

    # Create sensor object, using the board's default I2C bus.
    i2c = board.I2C()  # uses board.SCL and board.SDA
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

    # OR create sensor object, using the board's default SPI bus.
    # spi = board.SPI()
    # bme_cs = digitalio.DigitalInOut(board.D10)
    # bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

    # change this to match the location's pressure (hPa) at sea level
    bme280.sea_level_pressure = 1013.25
    #pid = PID(1, 0.1, 0.05, setpoint=29)

    return bme280.temperature, bme280.relative_humidity

    
    