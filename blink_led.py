import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

try:
  while(True):
    GPIO.output(14,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(14,GPIO.LOW)
    time.sleep(5)

except KeyboardInterrupt:
  GPIO.output(14, GPIO.LOW);
