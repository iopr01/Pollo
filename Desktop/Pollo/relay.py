from mimetypes import init
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

class realy():

    def __init__(self):

        self.RELAIS_1_GPIO = 17
        GPIO.setup(self.RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

    def on(self):
        GPIO.output(self.RELAIS_1_GPIO, GPIO.HIGH) # on
        
    def off(self):
        GPIO.output(self.RELAIS_1_GPIO, GPIO.LOW) # out