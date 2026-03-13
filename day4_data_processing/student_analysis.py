students = [
 {"name": "Rahul", "marks": 85},
 {"name": "Anita", "marks": 92},
 {"name": "Karan", "marks": 78},
 {"name": "Priya", "marks": 88}
]

for student in students:
    print(student['name'] + " - " + str(student['marks']))

max_marks = 0
total_marks = 0
topper = ""
for student in students:
    total_marks += student['marks']
    if(student['marks'] > max_marks):
        max_marks = student['marks']
        topper = student['name']

print(f"Topper: {topper} with marks {max_marks}")

print(f"Average Marks: {(total_marks / len(students))}")



