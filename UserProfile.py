"""
Create a dictionary to store a user's profile using the given inputs.

Input Format
First three lines contains: name (string), age (int), city (string)
Next three lines contains up to 3 hobbies
Last line contains the new age (int)


Output Format
Print original dictionary
Modify the dictionary with the following changes:
Add a new key-value pair: "is_active": True
Update the value of the "age" key.
Remove the "city" key from the dictionary.
Print the modified dictionary
Also Print number of hobbies


Sample 1:
Input
Alice
25
Delhi
Reading
Traveling
Cooking
30



Output
Original Dictionary:
{'name': 'Alice', 'age': 25, 'city': 'Delhi', 'hobbies': ['Reading', 'Traveling', 'Cooking']}
Modified Dictionary:
{'name': 'Alice', 'age': 30, 'hobbies': ['Reading', 'Traveling', 'Cooking'], 'is_active': True}


Number of hobbies: 3
"""


#cook your dish here
name=input()
age=int(input())
city=input()
my_list=[]
for i in range(3):
    hobby=input()
    my_list.append(hobby)
    

new_age=int(input())

print('Original Dictionary:')

my_dict={'name':name,'age':age,'city':city,'hobbies':my_list}
print(my_dict)

print('Modified Dictionary:')

my_dict['age']=new_age
my_dict['is_active']=True
my_dict.pop('city')
print(my_dict)

print(f'\nNumber of hobbies: {len(my_list)}')
