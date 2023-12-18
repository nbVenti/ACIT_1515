import requests
import sys

"""
Step 1 - Create the following variables:

Variable Name:          Data Type:          Initial Value:
--------------          ----------          --------------
word                    string              empty string
guessed                 set                 empty set
solution                list                empty list
incorrect               number              5
playing                 boolean             true
won                     boolean             false
"""
word = ""
guessed = set()
solution = []
incorrect = 5
playing = True
won = False


menu = [
    'Print the word',
    'View all guessed letters',
    'Check number of guesses remaining',
    'Guess a letter',
    'Guess the word'
]




"""
Step 2 - Make a GET request to 'https://random-word-api.herokuapp.com/word'

If the request is successful
    Extract the random word into the 'word' variable
    Fill the solution variable with underscores (so that the list is the same length as the random word)

Example:
    If the random word is 'python', the solution variable must be a list of length 6 and be filled with underscores, i.e.:
        ['_', '_', '_', '_', '_', '_']

    This is done so that we can print out the word to the user but show underscores for any letters that have not yet been guessed

If the request is not successful, immediately exit (stop the script) using sys.exit()
"""
response = requests.get("https://random-word-api.herokuapp.com/word")

if response.status_code == 200:
    word = response.json()[0]
    solution = ["_"] * len(word)
    # for __ in range(len(word)):
        # solution.append("_") 
    
else:
    sys.exit()



"""
Step 3 - Create a loop so that the user can repeatedly choose actions from a menu (menu actions are given to you above)

The loop should continue running as long as the playing variable is true AND the value of the incorrect variable is greater than zero.
"""
while playing and incorrect>0:  # CHANGE THIS LINE AS PER THE STEP 3 INSTRUCTIONS!




    """
    Step 4 - Inside the main loop, print the menu s(using the menu variable above)

    Use enumerate to print the menu out, one choice per line with a (one-based!) number,
        e.g.:

        1. Print the word
        2. View all guessed letters
        3. Check number of guesses remaining
        etc. 
    """
    print("\nMenu:")
    for index, item in enumerate(menu):
        print(f"{index + 1}. {item}")

    while True:
        user_input = input("\n>>")
        try: 
            user_input = int(user_input)
            if (user_input) > 0 and (user_input) <= len(menu):
                print()
                break
            else:
                print("Please enter a number between 1 and", len(menu), "\n" )
        except ValueError:
            print("Please enter a number between 1 and", len(menu), "\n")
    """  
    Step 5 - Inside the main while loop (from step 3), create a new while loop that never ends, prompting the user for their menu choice. 

    Inside this (new) while loop, use a try/except/else block to get a numeric choice from the user

    NOTE: your except block must catch specific errors related to converting the user input to a number. No except: with no exception/error name after it!

    If an exception is thrown, print a message for the user letting them know that they have to enter a number

    If no exception is thrown (and only if no exception is thrown!) break out of this inner loop
    """
    
    


    """ 
    Step 6 - Fill in the functionality below based on the user's menu choice.

    NOTE: replace the value True in the following if/elif/else statements with the name of the variable you created in the previous step!

    For example, if you call input() inside your try block, and store the result in a variable named choice, replace all the following True == x conditions with choice == x (where x is a number)
    """
    if user_input == 1: # CHANGE THIS LINE AS PER THE STEP 6 INSTRUCTIONS!
        """
        Print out the solution variable as a string, with spaces in between characters/underscores

        NO commas, NO square brackets, e.g.: _ _ _ _ _ _
        """
        print(" ".join(solution), "\n")
        
    elif user_input == 2: # CHANGE THIS LINE AS PER THE STEP 6 INSTRUCTIONS!
        """
        If no letters have been guessed yet, print a message to the user indicating that nothing has been guessed yet

        Otherwise, print out all guessed letters, with commas between them, e.g.: a,e,i,s,r
        """
        if len(guessed) == 0:
            print("Nothing has been guessed yet\n")
        else:
            print(",".join(guessed), "has been guessed\n")

    elif user_input == 3: # CHANGE THIS LINE AS PER THE STEP 6 INSTRUCTIONS!
        """  
        Print the number of guesses remaining 
        """
        print(f"You have {incorrect} guesses remaining\n")
        
    elif user_input == 4: # CHANGE THIS LINE AS PER THE STEP 6 INSTRUCTIONS!
        """
        Use input() to get the user to guess a letter

        If the guess is blank, or a number, print a message reminding them that they must enter an alphabet character

        If the guess is already in the guessed (set) variable, print a message to the user indicating that they have already guessed that letter

        If the guess is *not* in the set of guessed letters, do the following:
            1. Add the letter to the guessed set
            
            2. Check if the letter is *not* in the random word. If it is not in the word, subtract 1 from the incorrect variable and print a message telling the user they guessed incorrectly

            3. If the letter *is* in the random word, find every position where the letter occurs, write the letter into the solution list, and print a message to the user indicating that the letter they guessed was found

                NOTE: for this step, you MUST use a loop. NO list comprehensions, functions, etc.

                Example: 
                The program begins and the random word is 'driving'
                
                The solution list starts with length 7, filled with underscores:
                    ['_', '_', '_', '_', '_', '_', '_']
                
                The user chooses the letter 'i'. There are two i's, thus the solution now has the following values:
                    ['_', '_', 'i', '_', 'i', '_', '_']
                
                and would print out as:
                    _ _ i _ i _ _
        """
        
        user_input = input("\nGuess a letter\n>>")
        
            
        if user_input.isalpha():
            if len(user_input) >=2:
                print("Please enter a single letter\n")
                incorrect -= 1
            else:
                if user_input in guessed:
                    print("Guessed already\n")
                else:
                    guessed.add(user_input)
                    if user_input in word:
                        print("Correct\n")
                        for i in range(len(word)):
                            if word[i] == user_input:
                                solution[i] = user_input
                                
                        print(" ".join(solution),"\n")
                    else:
                        print("Incorrect\n")
                        incorrect -= 1
        else:
            print("Please enter a letter\n")
            incorrect -= 1
        
        if " ".join(solution).replace(" ", "") == (word):
            playing = False
            won = True
    else:
        """
        Use input() to allow the user to guess the word

        If they guess correctly, print a message to the user indicating they correctly guessed the word, set the playing variable to False (to stop the loop) and the won variable to True

        If they do not guess correctly, simply print a message to the user indicating that they were not correct
        """
        user_input = input("\nGuess the word\n>>")
        if user_input == word:
            print("Correct\n")
            playing = False
            won = True
        else:
            print("Incorrect\n")
            incorrect -= 1



"""
Step 7 - Print final output

If the user did not guess correctly (based on the value of the won variable), print a (supportive) message indicating that they did not guess the word

Regardless of whether the user won or lost, print a message telling them what the random word was
"""
if won:
    print("You won!\n")
else:
    print(f"You did not guess the word\n" )
print(f"The word was: {word}") 

"""
Step 8 - Test

Before submitting your script, test it thoroughly!

Ensure that:
    1. All menu actions work
    2. No invalid data is accepted
    3. No invalid characters are added to the guessed set
    4. No extra output is printed to the screen
    5. The random word is not shown to the user
"""