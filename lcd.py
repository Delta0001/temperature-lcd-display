# python lcd.py "message"
import sys
from RPLCD.gpio import CharLCD
from RPi import GPIO
GPIO.setwarnings(False)

# lcd = CharLCD(numbering_mode=GPIO.BOARD, pin_rs=27, pin_rw=25, pin_e=29, pins_data=[37, 35, 33, 31], cols=16, rows=2) # pin_rw is grounded
lcd = CharLCD(numbering_mode=GPIO.BCM, pin_rs=0, pin_e=5, pins_data=[26, 19, 13, 6], cols=16, rows=2)

lcd.clear()
lcd.write_string(sys.argv[1])

