a_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

'''
for i in range(0, 10):
    inp = input("Enter a number: ")
    # a_lists.append(int(inp))
    a_lists.append(inp)
'''



print(a_lists)

# del a_lists[7]

# print(a_lists[7])

# print(a_lists[9])

# length = len(a_lists)
# print(length)
# print(a_lists[::-2])


# a_lists = []
'''
for i in range(0, int(length/2 + 1)):
    print("index: {}".format(i))
    print(a_lists[i])
    del a_lists[i]
    print(a_lists)


while len(a_lists) > 0:
    tmp = a_lists.pop()
    print(tmp)


# del a_lists
print(a_lists)
'''

b_lists = []
for item in a_lists:
    if item % 2 == 0:
        b_lists.append(item)

print(b_lists)

c_lists = [item for item in a_lists if item % 2 == 0]
print(c_lists)
