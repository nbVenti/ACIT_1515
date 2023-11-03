if __name__ == "__main__":
    # While loop - runs one or more statments while a provided condition

    response = ""

    print("Before the loop")
    
    while response != "n":
        print("Inside the loop")
        response = input("Do you want to continue")

    counter = 0

    # careful INFINATE LOOP!
    # while True:
    #     counter = counter + 1
    #     print(counter)

    # using the break keyword

    while True:
        counter +=1 
        print(counter)
        if counter == 10:
            break

    # For loop - used to run one or more statements n amount of times
    # range()

    # range() - defines a range of numbers  
    print(range(3)) # defines the range 0 - 2
    range(1,5) # defines the range 1 - 4
    range(1,100,10)   
    range(100,0,-10)
    
    # letter in name
    
    guesses = int(input("How many guesses do you want"))

    for i in range(guesses):
        guess = input("Enter guess")

        # ig guess is lower than random number, print "Too low"
        # elif guess is higher then random number, print "Too high"
        #...

        print("Inside the for loop, i is equal to ", i )

print("after the loop")
