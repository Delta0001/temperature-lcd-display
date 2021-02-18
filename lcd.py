# python lcd.py "message"
import sys
import glob
from RPLCD.gpio import CharLCD
from RPi import GPIO

# GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(0, GPIO.OUT)  # RS
GPIO.setup(5, GPIO.OUT)  # E
GPIO.setup(6, GPIO.OUT)  # D4
GPIO.setup(11, GPIO.OUT) # V0
GPIO.setup(13, GPIO.OUT) # D5
GPIO.setup(19, GPIO.OUT) # D6
GPIO.setup(26, GPIO.OUT) # D7

# LCD Setup
lcd = CharLCD(numbering_mode=GPIO.BCM, pin_rs=0, pin_e=5, pins_data=[6, 13, 19, 26], cols=16, rows=2)
lcd.clear()

# Read Temperature
temperature_path = glob.glob('/sys/bus/w1/devices/28-*')[0] + "/temperature"
file = open(temperature_path)
raw_temp = file.read()

lcd.write_string(raw_temp)

