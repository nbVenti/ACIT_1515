import random

def prompt(message,valid_values,convert = None):
    response = None

    while True:
        response = input(f"\n{message} ")

        if convert:
            try:
                response = convert(response)
            except:
                print(f"Response must be of type {convert}")
                
        if response in valid_values:
            return response
        else:
            print(f"Response muse be in {valid_values}")        
        break

def main():
    #return # the function ends
    #return value # the function ends and a value is sent back to wherever the function is called
    keep_playing = True
    guessed_correctly = False

    while keep_playing:
        # promt the user for how many turns
        num_turns = prompt("How many turns do you want?",range(1,1001),int)
        # promt the for max value
        max_value = prompt("What is that max Value", range (1,101), int)

        #generate random 
        random_number = random.randint(1,max_value)

        #for loop
        for i in range(max_value):
            # prompt for a guess
            guess = prompt("Enter your guess:", range(1,max_value + 1),int)
            # tel the user too low, high, correct
            if guess < random_number:
                print("Too Low")
            elif guess > random_number:
                print("Too High")
            else:
                print("You are correct!")
                guessed_correctly = True
                break

        # if not guess correctly
        if not guessed_correctly:
            print("Sorry, you ran out if guesses")
            # tell the user they ran out of turns
        
        #prompt the user do you want to play again?
        play_again = prompt("Do you want to keep playng", ["y","n",""])

        if play_again == "n":
            keep_playing = False

main()