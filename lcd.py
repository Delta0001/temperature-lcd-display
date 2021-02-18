# python lcd.py
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

# Init values
temperature_path = glob.glob('/sys/bus/w1/devices/28-*')[0] + "/temperature"
previous_value_celcius = 0
previos_value_farenheit = 0

while(True):
    lcd.clear()
    # Read Temperature
    file = open(temperature_path)
    raw_temp = float(file.read())

    # Calculate Temperature
    value_celcius = raw_temp / 1000
    value_farenheit = (value_celcius * (9.0/5.0)) + 32

    # Display Temperature 
    lcd.write_string("Celcius: " + str(value_celcius))
    if previous_value_celcius < value_celcius:
        lcd.write_string("+")
    elif value_celcius < previous_value_celcius:
        lcd.write_string("-")

    lcd.crlf()

    lcd.write_string("Farenheit: " + str(value_farenheit))
    if previos_value_farenheit < value_farenheit:
        lcd.write_string("+")
    elif value_farenheit < previos_value_farenheit:
        lcd.write_string("-")

    previous_value_celcius = value_celcius
    previos_value_farenheit = value_farenheit
    sleep(1)
