from microbit import *
import random

# Randomly picking which actions to do
action = (str(random.randint(1, 2, 3)))

if action == 1:
    display_a()
    success = button_press(button_a)
    defeat = button_press(button_b)
    defeat = accelerometer.get_x_("shake") or accelerometer.get_z("shake")
elif action == 2:
    display_b()
    success = button_press(button_b)
    defeat = button_press(button_a)
    deafeat = accelerometer.get_x_("shake") or accelerometer.get_z("shake")
elif action == 3:
    display_shake()
    success = accelerometer.get_x_("shake") or accelerometer.get_z("shake")
    defeat = button_press(button_a, button_b)

# level and score progression
    if success:
        score = score + 1
        level = level + 1

    else:
        gameover = defeat
        gameover = True
        gameover = display.show(Image.SAD)

# game ending
sleep(1000)
while True:
    display.scroll("{} points".format(score))
