import random

# 1. Create a variable named keep_playing that stores the boolean value True
keep_playing = True

# 2. Create a variable named max_value that stores the number 13
max_value = 13

# 3. Create a while loop that will run until the play_again variable becomes False
# Note: the remaining answeres must be placed inside this while loop
while keep_playing:

    # 4. Create a variable named players that stores a list of four strings: "player1", "player2", "player3", and "player"
    players = ["player1","player2","player3","player4"]

    # 5. Create a variable named cards that stores an empty list
    cards = []

    # 6. Create a for loop that loops through all the values in the players list
    # Note: steps 7 and 8 should be placed inside this for loop
    for i in range(len(players)):

        # 7. Inside the for loop, create a variable named card that stores a random number between 1 and max_value (inclusive)
        card = random.randint(1,max_value)

        # 9. Append the list to the cards list
        cards.append(card)       


    # 10. End the for loop by printing the entire cards list on one line
    print(cards)

    # 11. Create a variable named unique that stores the cards list converted into a set
    unique = set(cards)


    # 12. Write an if statement that uses the cards list and unique variable to determine if any players drew a card of the same value
    if len(cards) != len(unique):

            # If more than one player picked a card of the same value, print a message indicating to the user that this hand is a draw, and allow the while loop to continue
            print("This Hand is a draw")

            # Else if no players picked a card of the same value, print a message to the user indicating who the winner was, and what the value of the card they picked was
                # e.g. Player 3 won the hand with a value of 12!
    else:
        i = 0
        u = 0 
        for x in range(len(cards)): 
            if i <= cards[x]:
                i = cards[x]
                u = x 
            

        print(players[u]+ " won the hand with a card vaulue of " + str(i))
        u = u + 1
        print(f"Player {u} won the hand with a card value of {i}")
        


        break
         
