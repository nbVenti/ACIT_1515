import random

keep_playing = True
num_guesses = 0
max_number = 0
random_number = 0
guess = 0
guesed_correctly = False

while keep_playing == True:
    
    for x in range(3):
        allowed_guesses = input("Enter max number of guesses:\n")
        if allowed_guesses == '':
            print("Please enter a number")
        else:
            break
    
    try:
        allowed_guesses = int(allowed_guesses)
    except:
        allowed_guesses = int(allowed_guesses,16)
    finally:
        max_number = allowed_guesses
        random_number = random.randint(1, allowed_guesses)
        print(random_number)

        for i in range(max_number):
            for y in range(3):
                guess = input("Enter guess\n")
                if guess == '':
                    print("please enter a number")
                else:
                    break

            try:
                guess = int(guess)
            except:
                guess = int(guess, 16)
            finally:
                if guess > random_number:
                    print("Too high")
                elif guess < random_number:
                    print("Too low")
                else:
                    print("Correct")
                    guesed_correctly = True
                    break
        if guesed_correctly == False:
            print("Sorry, you have fun out of guesses")

        response = input("Do you want to play again\n")
        if response == 'n':
            keep_playing = False
            exit()
