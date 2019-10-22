import microbit

while True:
    if microbit.button_a.is_pressed() and microbit.button_b.is_pressed():
        microbit.display.scroll("caleb")
        break
    elif microbit.button_a.is_pressed():
        microbit.display.scroll("asian")
    elif microbit.button_b.is_pressed():
        microbit.display.scroll("bitch")
    microbit.sleep(100)