import pyautogui
from utils.volume_control import set_volume
from utils.brightness_control import set_brightness

def execute_command(command):
    if command == "start_or_resume":
        pyautogui.press("f5")  # Or use spacebar depending on the application
    elif command == "exit":
        pyautogui.press("esc")
    elif command == "volume_up":
        set_volume("up")
    elif command == "volume_down":
        set_volume("down")
    elif command == "brightness_up":
        set_brightness("up")
    elif command == "brightness_down":
        set_brightness("down")
    elif command == "next_slide":
        pyautogui.press("right")
    elif command == "previous_slide":
        pyautogui.press("left")
    
    elif command == "scroll":
        pyautogui.scroll(-20)  # Example scroll command
