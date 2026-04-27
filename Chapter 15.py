"""
Chapter 15 Notes: Keeping Time, Scheduling Tasks, and Launching Programs
From: Automate the Boring Stuff with Python
"""

import time
import datetime
import subprocess
import webbrowser


# TIME MODULE
print("TIME MODULE")
print("Current timestamp:", time.time())

print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awake!\n")


# DATETIME MODULE
print("DATETIME MODULE")

dt = datetime.datetime(2025, 4, 27, 15, 30, 0)
print("Custom datetime:", dt)

now = datetime.datetime.now()
print("Current datetime:", now)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day, "\n")


# TIMEDELTA
print("TIMEDELTA")

delta = datetime.timedelta(days=7)
future_date = now + delta
print("Date after 7 days:", future_date, "\n")


# STRFTIME
print("STRFTIME")

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted, "\n")


# STRPTIME
print("STRPTIME")

date_str = "2025-04-27"
parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed datetime:", parsed_date, "\n")


# WAIT UNTIL TIME
print("WAIT UNTIL TIME")

target = datetime.datetime(2026, 1, 1)
print("Waiting until:", target)

while datetime.datetime.now() < target:
    time.sleep(1)

print("Happy New Year!\n")


# LAUNCH PROGRAM
print("LAUNCH PROGRAM")

# Windows example (uncomment to use)
# subprocess.Popen(['notepad.exe'])

# Linux example (uncomment to use)
# subprocess.Popen(['gedit'])


# OPEN FILE
print("OPEN FILE")

# Windows example (uncomment to use)
# subprocess.Popen(['start', 'file.txt'], shell=True)


# OPEN WEBSITE
print("OPEN WEBSITE")

webbrowser.open("https://www.google.com")


# SCHEDULING NOTE
print("\nSCHEDULING NOTE")
print("Use loops + sleep() or OS tools like Task Scheduler / cron.")
