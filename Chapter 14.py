"""
Chapter 14 - Working with CSV Files and JSON Data

Libraries:
- csv: read/write CSV files
- json: work with JSON data
"""

import csv
import json


# READING CSV FILES
def read_csv(file_name):
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


# Example
# read_csv('example.csv')


# WRITING CSV FILES
def write_csv(file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Age', 'City'])
        writer.writerow(['Alice', 25, 'London'])
        writer.writerow(['Bob', 30, 'Manchester'])


# Example
# write_csv('output.csv')


# USING DELIMITERS
def read_tsv(file_name):
    with open(file_name, newline='') as f:
        reader = csv.reader(f, delimiter='\\t')
        for row in reader:
            print(row)


# DICTIONARY CSV READER
def read_csv_dict(file_name):
    with open(file_name, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['Name'], row['Age'])


# DICTIONARY CSV WRITER
def write_csv_dict(file_name):
    with open(file_name, 'w', newline='') as f:
        fieldnames = ['Name', 'Age']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'Name': 'Alice', 'Age': 25})
        writer.writerow({'Name': 'Bob', 'Age': 30})


# JSON: CONVERT PYTHON -> JSON
def python_to_json():
    data = {
        'name': 'Alice',
        'age': 25,
        'city': 'London'
    }

    json_string = json.dumps(data)
    print(json_string)


# JSON: CONVERT JSON -> PYTHON
def json_to_python():
    json_string = '{"name": "Bob", "age": 30}'
    data = json.loads(json_string)

    print(data['name'], data['age'])


# SAVING JSON TO FILE
def save_json(file_name):
    data = {'name': 'Charlie', 'age': 35}

    with open(file_name, 'w') as f:
        json.dump(data, f)


# LOADING JSON FROM FILE
def load_json(file_name):
    with open(file_name) as f:
        data = json.load(f)
        print(data)


"""
Key ideas:
- CSV = simple table data (rows and columns)
- Use csv.reader() and csv.writer()
- DictReader/DictWriter use column names

- JSON = structured data (like dictionaries/lists)
- json.dumps() = Python -> JSON string
- json.loads() = JSON string -> Python
- json.dump()/load() = work with files

Tips:
- Always use newline='' when working with CSV files
- JSON is commonly used in APIs and web data
"""
