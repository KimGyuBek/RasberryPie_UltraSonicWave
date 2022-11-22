import RPi.GPIO as GPIO

ledPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

p = GPIO.PWM(ledPin, 255)
p.start(0)

while True:
   d = input("Enter Brightness(0 to 100) : ")  # LED 밝기 입력
   duty = int(d)                               # 입력받은 값이 정수인지 확인

   if(duty == 100):
      p.stop()
      GPIO.cleanup()
      break
   else:
      p.ChangeDutyCycle(duty)