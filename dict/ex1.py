import pprint

students = {}

department = 201
for i in range(1,  4):
    id = "{department}{counter}".format(department=department, counter=i)
    st_name = input("Enter Students Name: ")
    subjects = {}
    print("Please provide {name}\'s each subject marks: ".format(name=st_name))
    for item in range(0, 3):
        name = input("Subject {item}: ".format(item=item))
        marks = input("{name}\'s marks: ".format(name=name))
        subjects[name] = marks
        students[id] = {'name': st_name, 'subjects': subjects}

pprint.pprint(students)
