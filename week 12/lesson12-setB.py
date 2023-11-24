# while True:
#     try:
#         number = int(input("Please enter a value: "))
#     except:
#         # except: catches every error
#         print("Please enter a digit")
#     else:
#         print("no exception was raised/thrown") # only run when no exception was raised

"""
Python errors fall into two categories: syntax errors and runtime errors

Before running any part of your script, the Python interpreter checks for syntax errors (missing colons, indentation)

Every exception in python inherits from a base type called BaseException (this is "inheritance" in object-oriented)
"""


"""
SetBException
SetAException

try:
except SetBException:

try:
except (SetBException, SetAException) as e:
    print(e)

try:
except SetBException as e:
    print(e)
"""

"""
try/except blocks also accept an else block after the except - this block is only when no exception is raised
"""

"""
We can create custom exceptions in python as well as the built-in exceptions
"""
import sys

class InsufficientLengthException(Exception):
    pass

while True:
    try:
        password = input("Please enter your password: ")
        if len(password) < 8:
            raise InsufficientLengthException
    except InsufficientLengthException:
        print("Password must be at least 8 characters long")
    else:
        print("Thank you")
        sys.exit()

import time

# time.sleep() - pauses script execution for n seconds
while True:
    print("ACIT")
    time.sleep(5) # wait 5 seconds
    print("1515")

