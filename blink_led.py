import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(14, gpio.OUT)

while(True):
  gpio.output(14,gpio.HIGH)
  time.sleep(5)
  gpio.output(14,gpio.LOW)
  time.sleep(5)
