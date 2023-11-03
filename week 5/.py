from statistics import mean

# List Operations

grades = [50,60,70,90,10]
print(mean(grades))

# min(), max()
print(min(grades), max(grades))

# sum

# int(), str(), float(), list(), tuple()
print(list("ACIT_1515"))

grade = ("ACIT-1515", 90) 
grade_list = list(grade)
print(grade_list)

grade_tuple = tuple(grade_list)
print(grade_tuple, type(grade_tuple))

# grades = [50,60,70,90,10]
# for i in grades:
#     # no index, grade is assigned the value in the array one-by-one
#     grade = grades[i]
#     print(grade)

for grade in grades:    
    print(grade)

# enumerate() - steps through a list, and creates a tuple for each item in the list- the tuple contains (index, value)

# NOTE: enumerate() returns as enumerate object which can be converted into a list or iterated through
print(enumerate(grades))

for index, item in enumerate(grades):
    print(index, item)

# manipulating values in a list

# map(function, list)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def double(num):
    return num * 2

double_numbers = list(map(double, numbers)) # modified copy of numbers
# double_numbers = []

# for num in numbers:
#     double_numbers.append(num * 2)

print(double_numbers)

# create new list consisting of just the even numbers from the 'numbers' list
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# list comprehension
# new_list = [expression for item in list if condition]
new_numbers = [number for number in numbers if number > 5]
print(new_numbers)

courses = ["ACIT1515", "ACIT1630", "MATH1030", "COMM1020"]
acit_courses = [course + "!" for course in courses if "ACIT" in course]
print(acit_courses)

# -----------

# Command-line Arguments 
# py lab4.pt
"""
    * * * * 
    * * * * 
    * * * * 
    * * * * 


    board = [
        [EMPTY, EMPTY, EMPTY, EMPTY],  <-- row
        [EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY],
    ]
"""

board = [
    [0,1,2,3],
    [4,5,6,7],
    [8,9,10,11],
    [12,13,14,15]
]

for row in board:
    for column in row:
        print(column)

for i in range(len(board)):
    for j in range(len(board)):
        print(board[i][j])

ROWS = 4 

for i in range(ROWS):
    for j in range(ROWS):
        board[i][j]



