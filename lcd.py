# python lcd.py "message"
import sys
import glob
from RPLCD.gpio import CharLCD
from RPi import GPIO

# GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(0, GPIO.OUT)   # RS
GPIO.setup(5, GPIO.OUT)   # E
GPIO.setup(6, GPIO.OUT)   # D4
GPIO.setup(11, GPIO.OUT)  # V0
GPIO.setup(13, GPIO.OUT)  # D5
GPIO.setup(19, GPIO.OUT)  # D6
GPIO.setup(26, GPIO.OUT)  # D7

# LCD Setup
lcd = CharLCD(numbering_mode=GPIO.BCM,
              pin_rs=0, pin_e=5, pins_data=[6, 13, 19, 26],
              cols=16, rows=2)

temperature_path = glob.glob('/sys/bus/w1/devices/28-*')[0] + "/temperature"
while(True):
    lcd.clear()
    # Read Temperature
    file = open(temperature_path)
    raw_temp = float(file.read())

    value_celcius = raw_temp / 1000
    value_farenheit = (value_celcius * (9.0/5.0)) + 32

    # Show Temperature 
    lcd.write_string("Celcius: " + str(value_celcius))
    crlf()
    lcd.write_string("Farenheit: " + str(value_farenheit))

    sleep(1)


