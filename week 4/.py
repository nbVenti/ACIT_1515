import random

grades = []
message = ()
response = ()





def main():
    for i in range(7):
        x =  generate_random_number()
        grades.append(x)
    
    print("Your grades have been generated\n")
    for i in range(len(grades)):
        u = i +1
        print(f"{u}. {grades[i]}")

    while True:
        x = prompt("\n\nWhat would you want to do next?\n1. List grades\n2. Check Average\n3. Check Status\n4. Change grade\n5. Quit\n\nYour Response:")
        menu(x)
        

def generate_random_number():
    x = random.randint(0,100)
    return x
        
def prompt(message):
    x = input(message)
    try:
        x = int(x)
        return x 
    except:
        if x == "Quit":
            print("Quitting...")
            exit()
        else:
            print("Please input valid response")
            prompt(message)

def menu(y):
    if y == 1:
        for i in range(len(grades)):
            u = i +1
            print(f"{u}. {grades[i]}")
        while True:
            x = prompt("\n\n\nWould you like to continue? (y, x, "        ")\n\n")
            if x == "y" or x == "":
                return
            if x == "n" :
                print("Quitting...")
                exit()
            else:
                print("Please input a proper response")
        


    elif y == 2:
        x = return_average()
        print(f"Your average is {x}")

        while True:
            x = prompt("\n\n\nWould you like to continue? (y, x, "        ")\n\n")
            if x == "y" or x == "":
                return
            if x == "n" :
                print("Quitting...")
                exit()
            else:
                print("Please input a proper response")
    
    elif y == 3:
        x = return_average()
        print(f"Your average is {x}")
        if x >= 50:
            print("Passing")
        else:
            print("Failing")

        while True:
            x = prompt("\n\n\n\Would you like to continue? (y, x, "        ")\n\n")
            if x == "y" or x == "":
                return
            if x == "n" :
                print("Quitting...")
                exit()
            else:
                print("Please input a proper response")
    
    elif y == 4:
        print("Which grade would you like to change?")
        for i in range(len(grades)):
            u = i +1
            print(f"{u}. {grades[i]}")
        
        while True:
            x = prompt("Your response:")
            if x >= 1 and x <= 7:
                print(f"\nYou are changing course id {x} grade\nWhat would you like to change the grade to\n\n")
                y = prompt("Your response:")
                if y >= 1 and y <= 100:
                    grades[x-1] = y
                    for p in range(7):
                        o = p +1
                        print(f"{o}. {grades[p]}")
                    while True:
                        x = prompt("\n\n\n\Would you like to continue? (y, x, "        ")\n\n")
                        if x == "y" or x == "":
                            return
                        if x == "n" :
                            print("Quitting...")
                            exit()
                        else:
                            print("Please input a proper response")

                    break
                else:
                    print("Please input a vaild grade")
            else:
                print("Please input a vaild course id")
    
    else: 
        print("Quitting")
        exit()




def return_average():
    x = 0
    for i in range(len(grades)):
        x += grades[i]

    x = x / len(grades)
    return x
    


main()
