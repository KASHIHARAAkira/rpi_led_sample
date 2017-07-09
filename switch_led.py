import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while(True):
  GPIO.output(14,GPIO.HIGH)
  time.sleep(5)
  GPIO.output(14,GPIO.LOW)
  time.sleep(5)
  if GPIO.input(15) == 1:
    break
