"""

Assignment 1: Grades Generator
------------------------------

Assignment 1 is designed to test your understanding of the skills practiced in weeks 1 through 4:
- creating variables using Python's built-in data types
- converting and checking data types 
- using built-in functions
- using conditional statements and loops
- writing functions

For assignment 1 you will be writing a script that generates random grades and allows you to:
    a). View your randomly generated grades
    b). Get the average of your randomly generated grades
    c). Report your pass/fail status (i.e. if the average is above 50, you are passing. If the average is below 50 you are not yet passing)
    d). Change a grade
    e). Quit

Part 1:
-------
Begin by creating a variable named 'grades' that contains an empty list, i.e. grades = []

Next, write a for loop that runs seven times. Each time the loop runs, call the generate_random_number() function and append the returned number to the grades list

Once the grades have been generated, print a message to the user saying "Your grades have been generated."

Part 2:
-------
Create a while loop that runs indefinitely, e.g. while True:

Inside this loop, print out a menu for the user and list the possible actions they can take. Here is an example of how the output might look (but the wording and format is up to you):

    What would you like to do next?
    1. List Grades
    2. Check Average
    3. Check Status
    4. Change Grade
    5. Quit

Next prompt the user for their choice.

If they choose 1. List Grades
    a). output the grades using print()

If they choose 2. Check Average
    a). call the return_average function, passing in the grades variable
    b). inside the return_average function, calculate the current average (using any means of your choosing) and return the value
    c). back inside the main function, print the average you got back from return_average to the user

If they choose 3. Check Status
    a). again calculate the average using the return_average function
    b). write a conditional statement such that if the average is greater than 50, a message is printed to the user saying something like "Congratulations! You are passing.". If the average is lower than 50, write a (nice) message to the user saying something like "You're not currently passing, but I'm sure you will be by the end of the semester" or "You're not currently passing, there must be a mistake in the database!"

If they choose 4. Change Grades
    a). begin by printing out a list of their current grades, one per line with a number in front, e.g.:
        1. 65
        2. 74
        3. 89
        etc.
    b). next, prompt the user for which grade they would like to change
    c). after the user has chosen which grade to change, prompt them for the new grade
    d). use the values from b) and c) to index into the grades list and update the value

If they choose 5. Quit
    The program ends

"""

import random
# from tools import prompt

def generate_random_number():
    pass

def return_average(grades):
    pass

def main():
    pass

if __name__ == "__main__":
    main()