attributes = ['name', 'dob', 'gender']
values = [
['jason', '2000-01-01', 'male'],
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

list1 = []
for value in values:
    dict1 = {}
    for index,key in enumerate(attributes):
        print(index)
        dict1[key] = value[index]
    list1.append(dict1)
print(list1)