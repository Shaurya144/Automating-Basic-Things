import pyautogui

# Fail-Safe Feature
# Moving the mouse to the top-left corner of the screen
# will stop the program automatically.

pyautogui.FAILSAFE = True

# Pauses Between Actions
# Adds a short pause after every PyAutoGUI function call.

pyautogui.PAUSE = 1

# Screen Size

screen_width, screen_height = pyautogui.size()

print(screen_width, screen_height)

# Current Mouse Position

current_x, current_y = pyautogui.position()

print(current_x, current_y)

# Moving the Mouse

# Move instantly
pyautogui.moveTo(500, 300)

# Move over 2 seconds
pyautogui.moveTo(500, 300, duration=2)

# Move relative to current position
pyautogui.move(100, 0)

# Mouse Clicking

# Left click
pyautogui.click()

# Click at coordinates
pyautogui.click(500, 300)

# Double click
pyautogui.doubleClick()

# Right click
pyautogui.rightClick()

# Middle click
pyautogui.middleClick()

# Dragging the Mouse

# Drag to a position
pyautogui.dragTo(600, 400, duration=2)

# Drag relative to current position
pyautogui.drag(200, 0, duration=1)

# Scrolling

# Scroll up
pyautogui.scroll(500)

# Scroll down
pyautogui.scroll(-500)

# Typing Text

pyautogui.write("Hello world!")

# Typing with delay between characters
pyautogui.write("Typing slowly...", interval=0.25)

# Keyboard Presses

# Press a single key
pyautogui.press("enter")

# Press arrow keys
pyautogui.press("left")
pyautogui.press("right")

# Multiple key presses
pyautogui.press(["tab", "tab", "enter"])

# Holding Down Keys

pyautogui.keyDown("shift")
pyautogui.press("a")
pyautogui.keyUp("shift")

# Keyboard Shortcuts

# Ctrl + C
pyautogui.hotkey("ctrl", "c")

# Ctrl + V
pyautogui.hotkey("ctrl", "v")

# Taking Screenshots

# Capture the entire screen
screenshot = pyautogui.screenshot()

# Save screenshot
screenshot.save("screenshot.png")

# Locate an Image on the Screen

# Searches for an image on the screen
button_location = pyautogui.locateOnScreen("button.png")

print(button_location)

# Clicking an Image Automatically

button_center = pyautogui.locateCenterOnScreen("button.png")

if button_center is not None:
    pyautogui.click(button_center)

# Message Boxes

pyautogui.alert("This is an alert box.")

response = pyautogui.confirm("Continue?")

print(response)

user_text = pyautogui.prompt("Enter your name:")

print(user_text)

# Important Notes

# Coordinates start at:
# (0, 0) = top-left corner of screen

# X values increase moving right
# Y values increase moving down

# Common Uses of PyAutoGUI

# - Automating repetitive tasks
# - Filling forms automatically
# - Opening programs
# - Game automation
# - GUI testing
# - Data entry automation

# Safety Tips

# Always test automation carefully.
# Use duration arguments so mouse movement is visible.
# Keep FAILSAFE enabled.
# Avoid running scripts that click endlessly.

# Example Automation Script

import pyautogui
import time

time.sleep(5)

pyautogui.click(500, 300)
pyautogui.write("Automated text")
pyautogui.press("enter")
