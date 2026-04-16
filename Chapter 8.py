# String Literals
# escape sequences - eg using \
print('this is Tim \'s dog.')

''' for multiline comments '''

# there are also in and not in operators returning boolean statements

# f prefixes allow you to mix variables and strings

age = 40
print("in ten years I will be %s " % (age + 10))

# change the case of strings using .upper() and .lower()

'''
isalpha() Returns True if the string consists only of 
letters and isn’t blank

isalnum() Returns True if the string consists only of 
letters and numbers (alphanumerics) and isn’t blank

isdecimal() Returns True if the string consists only of 
numeric characters and isn’t blank

isspace()Returns True if the string consists only of 
spaces, tabs, and newlines and isn’t blank

istitle() Returns True if the string consists only of 
words that begin with an uppercase letter followed by only lowercase letters
'''

# you can use python to access the clipboard

import pyperclip
pyperclip.copy("Hello World")
pyperclip.paste()

text = "hello my name is shaurya and I like to eat pizza"
print(text)
answer = input("Would you like to copy this? Y/N").lower()

if answer ==  "y":
    pyperclip.copy(text)
    print("text copied")
else:
    print("ok no problem")