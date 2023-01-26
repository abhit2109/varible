def on_button_pressed_a():
    global Counter
    Counter = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Counter
    Counter = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Counter
    Counter = -1
input.on_button_pressed(Button.B, on_button_pressed_b)

Counter = 0
Counter = 0

def on_forever():
    basic.show_number(Counter)
basic.forever(on_forever)
