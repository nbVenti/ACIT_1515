"""

    ACIT 1515 - Lab 1

    For Lab 1 you must add code to this file sufficient to fulfill the following requirements:

    Part 1:
    -------
    Create a variable named current_year that stores the current year as an int
    Create a boolean variable named responded, set to False


    Part 2:
    -------
    For parts 3 to 6, you will use input() to prompt the user for a value, and store the value they enter into a variable.

    Users are allowed to skip answering the questions by simply hitting enter each time they are prompted for input, but not entering a value must not cause the script to crash!

    If a user answers even one of the next four questions, end the script by printing a message saying:
        Thank you for responding!

    If a user answers none of the questions, simply end the script without printing a message to the user


    Part 3:
    -------
    Use input() to prompt the user for the year they were born and store the result in a variable named birth_year.

    If the birth_year variable is not empty, print a message to the user saying:
        You are x years old
    (where x is equal to the value of current_year minus birth_year) then print a blank line


    Part 4:
    -------
    Use input() to prompt the user for their favorite number and store the result in a variable named fave

    If fave is not empty, print a message to the user saying:
        Your favorite number squared is x
    (where x is equal to their favorite number squared)

    If fave is not empty, print a message to the user saying:
        Your favorite number divided by two is x
    (where x is equal to their favorite number divided by two)

    If fave is not empty, and their favorite number is even, print a message to the user saying:
        Your favorite number is even
    otherwise, print a message saying:
        Your favorite number is odd

    Finally, print a blank line


    Part 5:
    -------
    Use input() to prompt the user for their first name and store the result in a variable called name

    If name is not empty, print a message to the user saying:
        Your name is x characters long
    (where x is the length of their name) then print a blank line


    Part 6:
    -------
    Use input() to prompt the user for a letter and store the result in a variable called letter

    If letter is not empty and the letter is part of the name they previously entered, 
    print a message to the user saying:
        Your name contains that letter
    otherwise, print a message to the user saying:
        Your name does not contain that letter


    IMPORTANT NOTES:
    ----------------

    You do not need to handle invalid data entered by the user. For example, if in Part 3 the user enters a value that cannot be converted to an integer, the script is allowed to crash and exit


"""

if __name__ == "__main__":
    