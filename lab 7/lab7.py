import json
import requests
from flask import Flask


def scrabble_score(word: str) -> int:
    LETTER_SCORES = {
        "a": 1,
        "b": 3,
        "c": 3,
        "d": 2,
        "e": 1,
        "f": 4,
        "g": 2,
        "h": 4,
        "i": 1,
        "j": 8,
        "k": 5,
        "l": 1,
        "m": 3,
        "n": 1,
        "o": 1,
        "p": 3,
        "q": 10,
        "r": 1,
        "s": 1,
        "t": 1,
        "u": 1,
        "v": 4,
        "w": 4,
        "x": 8,
        "y": 4,
        "z": 10,
    }
    score = 0
    for i in word:
        score += LETTER_SCORES[i]
    return score
    # calculate and return the score of the 'word' parameter
    


def get_computer_word() -> str:
    # use requests to GET https://random-word-api.herokuapp.com/word
    randWord = requests.get('https://random-word-api.herokuapp.com/word')

    if randWord.status_code == 200:
        randWord = randWord.json()
        return randWord[0]
    # if the status_code of the response is 200
        # convert response data into list using .json()
        # if converted data is not empty, return the word
    else:
        return "Error"
    # if status_code is not 200, return an error string
    pass # remove this line

def is_valid_word(player_word) -> bool:
    # get the length of player_word
    # use requests to GET f'http://localhost:5000/words/{len(player_word)}'
    word = {}
    # for i in range(len(player_word)):
    #     with open(f"lab 7/words/{i}-letter-words.json") as f:
    #         word[i] = json.load(f)
    # with open(f"lab 7/words/{len(player_word)}-letter-words.json") as f:
    #     word = json.load(f)

    # if player_word.status_code == 200:
    #     player_word = player_word.json()
    #     for i in word:
    #         if i == player_word:
    #             return True
            
    #     return False
    words = requests.get(f'http://127.0.0.1:5000/words/{len(player_word)}')
    word = words.json()
    for i in range(len(word)):
        if word[i]['word'] == player_word:
            print("Word found")
            return True
    print("Word not found")
    return False

    # if the status_code of the response is 200
        # convert response data into list using .json()
        # loop through list
            # if player_word is in the list, return True

    # if player_word was not found in list, return False
    pass # remove this line



def get_player_word(computer_word,) -> str:
    # create a variable called valid_input that is set to False
    valid_input = False

    # create a variable named word that is set to an empty string
    word = ""

    # create a while loop that runs while valid_input is False
    while not valid_input:
        # ask the user to input a word, store it in the word variable
        word = input("Please enter a word\n>>")
        print(word, type(word))
        
            # check if the word contains any numbers or symbols
        if word.isalpha():
            for i in word:
                if computer_word.__contains__(i):
                    valid_input = True
            if computer_word.__contains__(i) == False:        
                print("Not Valid, 1\n")
        else:
            print("Not Valid, 2\n")
    
        """
        check if the word contains any numbers or symbols
        

        if it does, print a message to the user telling them the word is not valid

        if the word does not contain any numbers or symbols, ensure the word contains at least one
        character from computer_word (if it doesn't contain at least one character from computer_word, print a message to the user letting them know the word is not valid)

        if the word contains no numbers or symbols, and at least one letter from computer_word, set valid_input to True
        """

    # return the word
    return word

def main() -> None:
    print("\nWelcome to One Shot Scrabble\n")
    print("Computer has 0 points and Player has 0 points\n")

    computer_score = 0
    player_score = 0

    computer_word = get_computer_word()
    computer_score = scrabble_score(computer_word)

    print(f"Computer chooses the {len(computer_word)} letter word '{computer_word}', for a score of {computer_score} points\n")

    valid_word = False

    while not valid_word:
        player_word = get_player_word(computer_word)
        
        valid_word = is_valid_word(player_word)
        
        if not valid_word:
            print(f"The {len(player_word)} character word {player_word} was not found. Please enter another word\n")

    player_score = scrabble_score(player_word)

    print(f"\nPlayer chose the {len(player_word)} letter word '{player_word}', for a score of {player_score} points\n")

    if player_score > computer_score:
        print("Player wins!\n")
    elif player_score == computer_score:
        print("Its a tie!\n")
    else:
        print("The computer wins!\n")


if __name__ == '__main__':
    main()
    