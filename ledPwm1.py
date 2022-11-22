#-*-coding: utf-8-*-
# 파일이름 : ledPwm1.py

import RPi.GPIO as GPIO
import time

ledPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

p = GPIO.PWM(ledPin, 255)

p.start(0)

try:
   while True:
      for i in range(20):
         p.ChangeDutyCycle(5*i)
         time.sleep(0.1)
      for i in reversed(range(20)):
         p.ChangeDutyCycle(5*i)
         time.sleep(0.1)

except KeyboardInterrupt:
   print()
   GPIO.cleanup()