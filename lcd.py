# python lcd.py "message"
import sys
from RPLCD.gpio import CharLCD
from RPi import GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

lcd = CharLCD(pin_rs=27, pin_rw=25, pin_e=29, pins_data=[37, 35, 33, 31], 
            cols=16, rows=2, 
            numbering_mode=GPIO.BOARD) # pin_rw is grounded

lcd.clear()
lcd.write_string(sys.argv[1])

