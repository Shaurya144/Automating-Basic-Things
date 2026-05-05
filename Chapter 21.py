import time

# time.time() returns the current time in seconds since the Unix epoch
current_time = time.time()
print(current_time)

# time.sleep() pauses execution for a given number of seconds
print("Start")
time.sleep(2)
print("2 seconds later")


# Rounding time values

# You can round time values for readability
rounded_time = round(time.time(), 2)
print(rounded_time)


# Using the datetime module

import datetime

# Get the current date and time
now = datetime.datetime.now()
print(now)

# Create a specific datetime object
dt = datetime.datetime(2025, 1, 1, 12, 0, 0)
print(dt)

# Access individual parts of the datetime
print(dt.year)
print(dt.month)
print(dt.day)


# Working with timedelta objects

# A timedelta represents a duration of time
delta = datetime.timedelta(days=7, hours=2)
print(delta)

# Add and subtract time
future = now + delta
print(future)

past = now - delta
print(past)


# Converting datetime to strings

# strftime() formats datetime into a string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

# Common format codes:
# %Y = year
# %m = month
# %d = day
# %H = hour (24-hour format)
# %M = minute
# %S = second


# Converting strings to datetime

# strptime() parses a string into a datetime object
date_string = "2025-12-25 15:30:00"
parsed = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed)


# Pausing until a specific date

# Example: wait until a future moment
target = datetime.datetime(2026, 1, 1, 0, 0, 0)

while datetime.datetime.now() < target:
    time.sleep(1)

print("Happy New Year!")


# Launching external programs

import subprocess

# Run another program (Windows example)
subprocess.Popen(["notepad.exe"])

# Open a file with its default application
subprocess.Popen(["start", "example.txt"], shell=True)


# Opening websites with webbrowser

import webbrowser

# Open a URL in the default browser
webbrowser.open("https://www.google.com")


# Basic task scheduling

# Example: run a task every 10 seconds
while True:
    print("Task running...")
    time.sleep(10)
