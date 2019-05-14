a_list = [1, 2, 3, 4, 5]
b_list = ["a", "b", "c"]

# b[1]

a_dict = {
    'a': 'rahul',
    'v': 'sandeep'
}

print(a_dict['v'])

b_dict = {
    1: 'rahul',
    2: 'sandeep'
}

print(b_dict[1])

c_dict = {
    'a': 'rahul',
    2: 'sandeep',
    'b': 'red'
}

print(c_dict[2])

d_dict = {
    'name': 'shelke',
    'firstname': c_dict,
    'list': a_list
}

print(d_dict)
print(d_dict['firstname']['b'])
print(d_dict['list'][2])


c_dict['c'] = "this"

print(c_dict)

c_dict.update({'d': 'that'})
print(c_dict)
c_dict.update({2: 1234})
print(c_dict)
c_dict[2] = 34556
print(c_dict)
