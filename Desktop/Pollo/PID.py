# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import RPi.GPIO as GPIO
import board
from adafruit_bme280 import basic as adafruit_bme280
from simple_pid import PID
import relay
#from scipy.interpolate import interp1d

def funcion1():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(24, GPIO.OUT)
    rojo = GPIO.PWM(24, 100) #optu a dimmr para control
    rojo.start(100)
    # Create sensor object, using the board's default I2C bus.
    i2c = board.I2C()  # uses board.SCL and board.SDA
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

    control_vent = relay.realy()
    
    # OR create sensor object, using the board's default SPI bus.
    # spi = board.SPI()
    # bme_cs = digitalio.DigitalInOut(board.D10)
    # bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

    # change this to match the location's pressure (hPa) at sea level
    bme280.sea_level_pressure = 1013.25

    #PID
    pid = PID(304.5, 626.5, 0, setpoint=28.8)

    # Assume we have a system we want to control in controlled_system
    #v = controlled_system.update(0)

    # Compute new output from the PID according to the systems current value
    control = pid(bme280.temperature)
        
    if control >= 100:
        control = 100
    elif control <= 0:
        control = 0
    rojo.ChangeDutyCycle(control)

    if bme280.temperature > 40:
        control_vent.on()
    else:
        control_vent.off()

    return bme280.temperature, bme280.humidity