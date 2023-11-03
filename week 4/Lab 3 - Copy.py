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
    keep_playing = True
    guessed_correctly = False

    while keep_playing:
        num_turns = prompt("How many turns do you want?",range(1,1001),int)
        max_value = prompt("What is that max Value", range (1,101), int)

        random_number = random.randint(1,max_value)

        for i in range(num_turns):
           
            guess = prompt("Enter your guess:", range(1,max_value + 1),int)
        
            if guess < random_number:
                print("Too Low")
            elif guess > random_number:
                print("Too High")
            else:
                print("You are correct!")
                guessed_correctly = True
                break
 
        if not guessed_correctly:
            print("Sorry, you ran out if guesses")
          
        play_again = prompt("Do you want to keep playng", ["y","n",""])

        if play_again == "n":
            keep_playing = False

main()