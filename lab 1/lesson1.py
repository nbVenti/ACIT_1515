# KEYBOARD SHORTCUTS

# CTRL-N - new file 
# CTRL-SHIFT-S - save-as
# CTRL-S save
# CTRL-~ to open terminal inside VSCode
# CTRL-Enter to jump to next line
# CTRL-Shift-Enter create line above
# Shift-Alt-Down - duplicate line
# Ctrl-Shift-K / Shift-Delete - delete line(s)
# Ctrl-D - selects the next instance of whatever is selected
# Alt-Click - add more cursors

# python scripts end with .py extension

# CTRL-c stops a running script

if __name__ == "__main__":
    # == - equality operator
    
    # = - assignment operator, for creating (or updating) variables that can store values in our scripts
    course_number = 1515
    course_number = "1515" # data type (i.e. string, number) can be changed freely in python
    school = "BCIT"
    program = 'CIT' # strings can be surrounded by either single or double quotes
    keep_playing = True

    # all indented lines below 'while' will run repeatedly until keep_playing becomes false
    while keep_playing == True:

        # read string input from user and convert to an integer
        guess = int(input("Guess a number: "))

        if guess == 6:
            print("Correct")

        # get input from user - whatever the user types is returned as a string
        response = input("Do you want to keep playing? ")

        if response == "no":
            keep_playing = False # setting variable to False means that while loop will stop

    print("Bye!")
