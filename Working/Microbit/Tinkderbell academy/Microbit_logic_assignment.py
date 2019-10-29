from microbit import *
import random

# Randomly picking which actions to do
action = random.randint(1, 2, 3)

if action == 1:
    display_a()
    success = button_press(button_a, button_b)
elif action == 2:
    display_b()
    success = button_press(button_b, button_a)
elif action == 3:
    display_shake()
    success = accelerometer.get_x_("shake") or accelerometer.get_z("shake")

# level and score progression
    if success:
        score = score + 1
        level = level + 1

    else:
        display.show(Image.SAD)
        gameover = True

# game ending
sleep(1000)
while True:
    display.scroll("{} points".format(score))
