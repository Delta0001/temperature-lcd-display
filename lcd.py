# python lcd.py "message"
import sys
from RPLCD.gpio import CharLCD
from RPi import GPIO
GPIO.setwarnings(False)

lcd = CharLCD(pin_rs=27, pin_e=29, cols=16, rows=2, pins_data=[37,35,33,31], numbering_mode=GPIO.BOARD)

lcd.clear()
lcd.write_string(sys.argv[1])

