# Like a list, a dictionary is a mutable collection of many values.
# but unlike a list, indexes for dictionaries contain many different data types

customers = {"ID": 1, "Name": "John", "Age": 23}
print(customers["ID"])

birthdays = {'Shaurya': 'Apr 1', 'James': 'Dec 12', 'Ben': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(name +"'s birthday is on "+ birthdays[name])
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
