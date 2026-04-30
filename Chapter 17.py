# Chapter 17 – Keeping Time, Scheduling Tasks, and Launching Programs

import time
import datetime
import subprocess
import webbrowser

# time module basics

now_timestamp = time.time()
print(now_timestamp)

time.sleep(3)

# datetime basics

now = datetime.datetime.now()
print(now)

specific_date = datetime.datetime(2026, 4, 30, 12, 0, 0)
print(specific_date)

print(specific_date.year)
print(specific_date.month)
print(specific_date.day)
print(specific_date.hour)

# timedelta (durations)

delta = datetime.timedelta(days=7, hours=2)
print(delta)

future = now + delta
past = now - delta

print(future)
print(past)

# formatting dates (strftime)

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

# parsing dates (strptime)

date_string = "2026-04-30 15:30:00"
parsed = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed)

# comparing dates

if now > parsed:
    print("Now is later")

# working with readable time

local_time = time.localtime()
print(local_time)

readable_time = time.asctime(local_time)
print(readable_time)

# launching programs

# subprocess.Popen(['notepad.exe'])  # Windows
# subprocess.Popen(['start', 'file.txt'], shell=True)
# subprocess.run(['ls', '-l'])  # Linux / Mac

# opening websites

webbrowser.open("https://www.python.org")

# simple scheduled loop

print("Start of program")

while True:
    print("Task running...")
    time.sleep(10)

# simple timer

print("Timer started for 5 seconds...")
time.sleep(5)
print("Time's up!")

# countdown example

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("Go!")

# key points

# time.time() gives timestamp
# time.sleep() pauses code
# datetime handles dates and times
# timedelta represents durations
# strftime formats datetime to string
# strptime parses string to datetime
# subprocess launches programs
# webbrowser opens URLs
# loops + sleep can be used for scheduling
