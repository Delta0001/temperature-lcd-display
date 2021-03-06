# python lcd.py
import glob
import time
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
lcd.clear()

# Init values
temperature_path = glob.glob('/sys/bus/w1/devices/28-*')[0] + "/temperature"
previous_value_celcius = 0
count = 0

while(True):
    lcd.home()  # reset cursor to beginning
    # Read Temperature
    file = open(temperature_path)
    try:
        raw_temp = float(file.read())
    except:
        continue

    # Calculate Temperature
    value_celcius = round(raw_temp / 1000, 2)
    value_farenheit = round((value_celcius * (9.0/5.0)) + 32, 2)

    # Display Temperature
    lcd.write_string("Temperature")

    if (count%2 == 0):
        lcd.write_string(":")
    else:
        lcd.write_string(" ")
    count=count+1
    
    lcd.crlf()

    lcd.write_string('{:.2f}'.format(value_celcius) + "C")
    if previous_value_celcius < value_celcius:
        lcd.write_string(" + ")
    elif value_celcius < previous_value_celcius:
        lcd.write_string(" - ")
    else:
        lcd.write_string("   ")

    lcd.write_string('{:.2f}'.format(value_farenheit) + "F")

    previous_value_celcius = value_celcius
    time.sleep(0.5)
