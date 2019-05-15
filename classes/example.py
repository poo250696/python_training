import prblm7

a_list = [1, 2, 3, 4, 5]

print(a_list[2])

b_dict = {
    'a': 'AAA',
    'b': 'BBB'
}

print(b_dict['b'])


c_module = prblm7.is_prime(47)
print(c_module)

print(prblm7.TEST_PRINT)


class Test(object):

    def __init__(self, name):
        self.test = name

    def print_test(self):
        return self.test


test_obj = Test(27)
print(test_obj.print_test())
test_obj.test = 49
print("Self: ", test_obj.test)
print("Method: ", test_obj.print_test())


class Example(object):

    def __init__(self):
        self.first = None # first
        self.last = None # last

    def print_name(self):
        return "{0} {1}".format(self.first, self.last)


example_obj = Example()  # "Rahul", "Shelke")
print(example_obj.print_name())
print(example_obj.first)
print(example_obj.last)
example_obj.first = "Sandeep"
example_obj.last = "Chintala"
print(example_obj.print_name())

