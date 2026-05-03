import time

# Get current time in seconds since Unix epoch
current_time = time.time()

# Pause execution
time.sleep(2)

# Convert timestamp to local time tuple
local_time = time.localtime(current_time)

# Convert timestamp to readable string
readable_time = time.ctime(current_time)


# Using datetime module

import datetime

# Current date and time
now = datetime.datetime.now()

# Create a specific datetime
dt = datetime.datetime(2025, 1, 1, 12, 0, 0)

# Access components
year = now.year
month = now.month
day = now.day
hour = now.hour


# timedelta objects

# Represent a duration
delta = datetime.timedelta(days=7)

# Add and subtract time
future = now + delta
past = now - delta


# Formatting dates with strftime

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

# Common format codes
# %Y year
# %m month
# %d day
# %H hour (24-hour)
# %M minute
# %S second


# Parsing dates with strptime

parsed_date = datetime.datetime.strptime("2025-01-01", "%Y-%m-%d")


# Scheduling tasks (basic loop example)

while False:
    print("Task running...")
    time.sleep(60)


# Launching external programs

import subprocess

# Run a program (example may vary by OS)
subprocess.Popen(["notepad.exe"])

# Run command and capture output
result = subprocess.run(["echo", "Hello"], capture_output=True, text=True)
output = result.stdout


# Opening web pages

import webbrowser

webbrowser.open("https://example.com")
