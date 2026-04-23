# Reading and Writing Files
# A file has two key properties: a filename
# (usually written as one word) and a path. The path specifies
# the location of a file on the computer

from pathlib import Path
p = Path('spam.txt')
p.write_text('Hello, world!')
p.read_text()
content = p.read_text()
print(content)