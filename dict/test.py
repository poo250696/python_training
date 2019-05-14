names = {
    'first': 'Rahul',
    'last': "Shelke",
    'middle': "Baban"
}

print(names)

for key, value in names.items():
    print("{0} => {1}".format(key, value))

for key in names:
    # del names[key]
    print("{0} => {1}".format(key, names.get(key, None)))

del names['middle']

# print(names['middle'])
print(names.get('middle', "No middle name provided"))
