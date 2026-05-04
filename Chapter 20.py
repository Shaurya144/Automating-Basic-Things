# Chapter 20: Controlling the Keyboard and Mouse with GUI Automation

import pyautogui
import time

# PyAutoGUI lets Python control the mouse and keyboard
# Useful for automating repetitive GUI tasks

# Safety Feature
# Moving mouse to top-left corner raises FailSafeException
pyautogui.FAILSAFE = True

# Pause after each PyAutoGUI call (in seconds)
pyautogui.PAUSE = 0.5

# Screen Information
screen_width, screen_height = pyautogui.size()
print("Screen size:", screen_width, screen_height)

current_mouse_x, current_mouse_y = pyautogui.position()
print("Current mouse position:", current_mouse_x, current_mouse_y)

# Mouse Movement
pyautogui.moveTo(200, 200, duration=1)  # move to (200, 200)
pyautogui.move(100, 0, duration=1)      # move right 100 pixels

# Mouse Clicks
pyautogui.click()                       # click at current position
pyautogui.doubleClick()
pyautogui.rightClick()

# Dragging
pyautogui.moveTo(300, 300, duration=1)
pyautogui.dragTo(400, 400, duration=1)

# Scrolling
pyautogui.scroll(200)   # scroll up
pyautogui.scroll(-200)  # scroll down

# Keyboard Input
pyautogui.write("Hello, this is automated typing!", interval=0.05)
pyautogui.press("enter")

# Key combinations (hotkeys)
pyautogui.hotkey("ctrl", "a")  # select all
pyautogui.hotkey("ctrl", "c")  # copy

# Screenshot
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

# Locate image on screen (requires image file available)
# button_location = pyautogui.locateOnScreen("button.png", confidence=0.8)
# if button_location:
#     pyautogui.click(pyautogui.center(button_location))

# Simple GUI dialogs
pyautogui.alert("This is an alert box")
response = pyautogui.confirm("Do you want to continue?")
print("User response:", response)

user_input = pyautogui.prompt("Enter your name:")
print("User input:", user_input)

# Best Practice Example
# Add delay so user can prepare (e.g., switch window)
print("Starting automation in 5 seconds...")
time.sleep(5)

# Example automation: open run dialog and type something (Windows only)
pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("notepad")
pyautogui.press("enter")

# this concludes chapter 20