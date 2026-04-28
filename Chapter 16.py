# CSV = Comma-Separated Values
# Used for simple tabular data (like spreadsheets)

import csv

# Reading CSV files
with open('example.csv') as file:
    reader = csv.reader(file)
    data = list(reader)  # converts to list of rows

# Each row is a list
# data[row][column]

# Example:
# data[0] -> first row
# data[0][1] -> second column of first row

# Looping through CSV
with open('example.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing CSV files
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', '30', 'London'])

# newline='' prevents blank rows on Windows

# Delimiters and formatting
csv.writer(file, delimiter='\t')   # tab-separated
csv.writer(file, quoting=csv.QUOTE_MINIMAL)

# Easier way to work with CSV using dictionaries

# DictReader
with open('example.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Name'])  # access by column name

# DictWriter
with open('output.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'Name': 'Bob', 'Age': 25})

# JSON = JavaScript Object Notation
# Common for APIs and config files

import json

# Converting Python -> JSON
data = {
    'name': 'Alice',
    'age': 30,
    'is_student': False
}

json_string = json.dumps(data)  # convert to JSON string

# Writing JSON to file
with open('data.json', 'w') as file:
    json.dump(data, file)

# Converting JSON -> Python
json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)

# Reading JSON from file
with open('data.json') as file:
    data = json.load(file)
