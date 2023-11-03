"""
    This file contains 9 errors,
    6 of which are syntax errors, 3 of which are logical errors

    You must fix all the errors such that the script prints out:
    The factorial of 10 is 3628800 
    
    Note the number above is three million, six-hundred and twenty-eight thousand, eight hundred

    RULES:

    You *cannot* add or remove any lines in your final submission (though you *will* need to temporarily add print statements to debug)

    You *can* change the order of statements in the script with the following exceptions:
        Any statements currently inside the while loop must stay inside the while loop
        Any statements outside the while loop must stay outside the while loop 

    You *can* change variable values and operators if necessary
"""

if __name__ == "__main__":
    num = 10
    result = 1

    # calculate the factorial of 10
    while True:
        result = result * num
        num = num-1
        print(result)

        if num == 1:
            break

    if result != -1:
        print(f"The factorial of 10 is {result}")
