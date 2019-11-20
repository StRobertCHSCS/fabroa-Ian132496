from microbit import *
import random

while True:
# Randomly picking which actions to do
            action = (random.randint(1, 3)

    if action == 1:
        display_a()
        success = microbit.button_a.is_pressed()
        defeat = microbit.button_b.is_pressed()
        defeat = accelerometer.get_x_("shake") or accelerometer.get_z("shake")
        newAction();
        elif action == 2:
        display_b()
        success = microbit.button_b.is_pressed()
        defeat = microbit.button_a.is_pressed()
        defeat = accelerometer.get_x_("shake") or accelerometer.get_z("shake")
        newAction();
    elif action == 3:
        display_shake()
        success = accelerometer.get_x_("shake") or accelerometer.get_z("shake")
        defeat = microbit.button_a.is_pressed() and microbit.button_b.is_pressed()
        newAction();

    else:
        defeat = display.show(Image.SAD)
        defeat = microbit.sleep()

# When game's not being played
while False:
    microbit.sleep()
