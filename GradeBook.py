"""
You are given a list of operations to perform on a student gradebook.
Each operation is represented as a tuple and can be one of the following type

("add", name, grade) – Add a student with their grade.
("modify", name, new_grade) – Update an existing student's grade.
("remove", name) – Remove a student.
("access", name) – Access and store a student's grade.
After processing all operations, print the results in given format.

Input Format
A single list named operations, which contains multiple tuples.
Each tuple represents an operation to perform .

Output Format
Print two lines:
The final gradebook as a dictionary in the format:
Final Gradebook: {name: grade, ...}
The accessed grades list in the format:
Accessed Grades: [grade1, grade2, ...]

Sample 1:
Input
[('add', 'Alice', 85), ('add', 'Bob', 92), ('access', 'Alice')]

Output
Final Gradebook: {'Alice': 85, 'Bob': 92}
Accessed Grades: [85]
"""

import ast

n = input().strip()
data = ast.literal_eval(n)
my_dict = {}
key = []

for i in data:
    if i[0].lower()== 'add':
        my_dict[i[1]] = int(i[2])
    elif i[0].lower()=='modify' and i[1] in my_dict:
        my_dict[i[1]]=int(i[2])
    elif i[0].lower() == 'remove':
        my_dict.pop(i[1], None)
    elif i[0].lower() == 'access' and i[1] in my_dict:
        key.append(my_dict[i[1]])

print(f'Final Gradebook: {my_dict}')

if key!=[]:
    print(f'Accessed Grades: {key}')
