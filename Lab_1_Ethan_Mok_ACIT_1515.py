currYear = int(2023)
responded = False


birthYear = (input("Enter birth year"))

if birthYear == '':
    responded = False
    birthYear = "skipped"
    favNum = input("Favourite number")
    if favNum == '':           
        responded = False
        favNum = "skipped"
        firstName = input("Enter first name")
        if firstName == '':
            firstName = "skipped"
            responded = False
            letter = input("Enter a letter")
            if letter == '':
                exit()
            
            
            
            else:
                print("Your name does not contain that letter\n")
                responded = True
        else:
            firstName = str(firstName)
            print("Your name is " + str(len(firstName))+ "characters long\n")
            responded = True
    else: 
            favNum = int(favNum) 
            y = favNum * favNum
            y = str(y)
            print("Your favorite number squared is " + y)
            u = favNum / 2
            u = str(u)
            print(f"Your fav number divided by 2 is " + u)
            i = favNum % 2
            if i == 1:
                print("Fav number is odd\n")
            else:
                print("Fav number is even\n")
            responded = True     
else:
    birthYear = int(birthYear)
    x = currYear - birthYear
    x = str(x)
    print("You are " + x + " years old\n")
    print()
    responded = True
    
if responded == True:
    print("Thank you for responding")







