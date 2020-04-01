#!/usr/bin/python3
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import json

x = 0
y = 0
m = 0
sense = SenseHat()


def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = y - 1

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = y + 1

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = x - 1

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = x + 1
def pushed_middle(event):
    global m
    if event.action != ACTION_RELEASED:
        m = m + 1

def refresh():
    sense.clear()
    sense.set_pixel(x, y, 255, 255, 255)
    data = json.dumps({"x": x, "y": y,"m": m})
    f = open("joystick.dat", "w")
    f.write(data)
    f.close()


sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle
sense.stick.direction_any = refresh
refresh()
pause()
