currYear = int(2023)
responded = False




for __ in range(3):
    birth_year = input("input birth year\n\n")
    if birth_year != '':
        try: 
            birth_year = int(birth_year)
        
            if isinstance(birth_year, int) == True:
                responded = True 
                birth_year = int(birth_year)
                x = currYear - birth_year
                x =  str(x)
                print(f"\nYou are {x} years old\n ")
                break
        except: 
            print("Please input a year")
    else:
        print("\n")
        break

fave = input("\nInput number\n\n")

if fave != '':
    try:
        fave = int(fave)
        if isinstance (fave, int) == True:
            responded = True
            fave = int(fave)
            print(f"Ur fave number ^2 = {fave ** 2} ")
            print(f"ur fave number /2 = {fave / 2}")
            if fave % 2 == 1:
                print("ur fave number is odd\n")
            else:
                print("ur fave number is even\n")
    except:
        fave = int(fave,16)
        print(f"Ur fave number ^2 = {fave ** 2} (hexadecimal)")
        print(f"ur fave number /2 = {fave / 2} (hexadecimal)")
        if fave % 2 == 1:
            print("ur fave number is odd (hexadecimal)\n")
        else:
            print("ur fave number is even (hexadecimal)\n")
        


else:
    print("\n")


name = input("\nname\n\n")
print("\n")
y = 0
for __ in range(len(name)):
    y += 1
    
print(f"Nme is {y} chars long\n")


letter = input("leter\n\n")
while letter != '':
    if name.find(letter) != -1:
        print("letter found \n")
        break
    else:
        print("letter not in name\n")
        break


print(f"Responded = {responded}")
if responded == True:
    print("You ahve fill out the survy")

