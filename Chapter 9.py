# Text Pattern Matching with regular expression

def is_phone_number(text):
    if len(text) != 11:
        return False
    for i in range(0,11):
        if not text[i].isdigit():
            return False
    return True

answer = input("write a phone number: ")
print(is_phone_number(answer))
# UK phone numbers eg 07294392759


message = 'Call me at 08294592852 tomorrow. 07294392759 is my office.
for i in range(len(message)):
  segment = message[i:i+11]
  if is_phone_number(segment):
        print('Phone number found: ' + segment)

print('Done')

# Regular expressions, called regexes for short,
# are a sort of mini language that describes a pattern of text.

#

import re
phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.')
match_obj.group()

# did not understand much of this chapter so will come back after chapter 10
