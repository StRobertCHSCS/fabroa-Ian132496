# Write your code here :-)
from microbit import *
import music 
 
# pins
ADKeypad_pin = pin2
Buzzer_pin = pin0
 
while True:
    # buttonA 
    if ADKeypad_pin.read_analog() > 50 and ADKeypad_pin.read_analog() < 50:
        music.play('f3:4', pin=Buzzer_pin)
     
    # buttonB 
    if ADKeypad_pin.read_analog() > 95 and ADKeypad_pin.read_analog() < 50:
        music.play('g3:4', pin=Buzzer_pin)
 
    # buttonC 
    if ADKeypad_pin.read_analog() > 140 and ADKeypad_pin.read_analog() < 50:
        music.play('a3:4', pin=Buzzer_pin)
     
    # buttonD 
    if ADKeypad_pin.read_analog() > 40 and ADKeypad_pin.read_analog() < 50:
        music.play('b3:4', pin=Buzzer_pin)
     
    # buttonE 
    if ADKeypad_pin.read_analog() > 0 and ADKeypad_pin.read_analog() < 50:
        music.play('c2:4', pin=Buzzer_pin)