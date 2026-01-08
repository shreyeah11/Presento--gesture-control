import screen_brightness_control as sbc

def set_brightness(direction):
    current = sbc.get_brightness(display=0)[0]
    if direction == "up":
        sbc.set_brightness(min(current + 10, 100), display=0)
    elif direction == "down":
        sbc.set_brightness(max(current - 10, 0), display=0)
