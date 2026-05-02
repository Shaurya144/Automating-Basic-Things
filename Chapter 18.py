import time
import datetime
import subprocess
import os
import math


print("Current timestamp:", time.time())

# Measure execution time
start = time.time()
for i in range(1000000):
    pass
end = time.time()
print("Time taken:", end - start, "seconds")

# DATETIME MODULE
now = datetime.datetime.now()
print("Current datetime:", now)

# Create a specific datetime
dt = datetime.datetime(2026, 5, 2, 12, 0, 0)
print("Custom datetime:", dt)

# Format datetime
formatted = now.strftime('%Y-%m-%d %H:%M:%S')
print("Formatted datetime:", formatted)

# TIME ARITHMETIC (timedelta)
delta = datetime.timedelta(days=7)
future = now + delta
print("One week from now:", future)

# PAUSING EXECUTION
print("Pausing for 2 seconds...")
time.sleep(2)
print("Resumed!")

# ROUNDING NUMBERS
num = 3.75
print("Round:", round(num))
print("Floor:", math.floor(num))
print("Ceil:", math.ceil(num))

# SIMPLE SCHEDULING LOOP
print("Checking time every second (runs 5 checks)...")

checks = 0
while checks < 5:
    current = datetime.datetime.now()
    print("Current time:", current.strftime('%H:%M:%S'))
    time.sleep(1)
    checks += 1

# LAUNCHING EXTERNAL PROGRAMS
# NOTE: This example may vary depending on your OS

try:
    print("Attempting to open a program...")
    subprocess.Popen(['notepad.exe'])  # Windows example
except Exception as e:
    print("Could not open program:", e)

# OPENING FILE WITH DEFAULT APP
try:
    print("Attempting to open a file...")
    os.startfile('example.txt')  # Windows only
except Exception as e:
    print("Could not open file:", e)

# PRACTICAL EXAMPLE: SIMPLE REMINDER
print("Reminder will trigger in 5 seconds...")
time.sleep(5)
print("Reminder: Take a break!")