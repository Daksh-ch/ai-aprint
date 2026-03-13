import json

with open('students.json') as file:
    data = json.load(file);  #loads the content from a json file into a dictionary
print(data) #prints the content of the json file as a dictionary

data2 = [{'name': 'John', 'age': 25, 'city': 'New York'},{'name': 'Alan', 'age': 35, 'city': 'Chicago'},{'name': 'Alice', 'age': 30, 'city': 'Boston'},{'name': 'Bob', 'age': 28, 'city': 'Seattle'}] #creates a dictionary

with open('employees.json','w') as file:
    json.dump(data2, file)

    