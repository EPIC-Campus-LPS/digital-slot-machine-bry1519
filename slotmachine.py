import time
import random
import board
import tm1637 
from gpiozero import Button
import RPi.GPIO as GPIO
BUTTOM_PIN = (6)
LED_GREEN = 18
display = tm1637.TM1637(clk=5, dio=4)
display.brightness(2)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(6, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def onandoff_LED():
	for _ in range(3):
		GPIO.output(18, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(18, GPIO.LOW)
		time.sleep(0.2)

def show_random():
	number = random.randint(1111, 9999)
	tm.write(clear)

try:
	while True:
		if GPIO.input(6) == GPIO.LOW:
			number = random.randint(1111, 9999)
			display.number(number)
			if number != 0 and number % 1111 == 0:
				print (f"{number}")
				onandoff_LED()
			elif number == 1111:
				onandoff_LED
			time.sleep(0.05)
		else:
			time.sleep(0.1)

	time.sleep(0.1)
except KeyboardInterrupt:
	display.write([0, 0, 0,])
	GPIO.cleanup()

