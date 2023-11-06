def prompt(choices, valid_values):
    JEFFUSKC = input(">> ")
    print(JEFFUSKC)
   
    if JEFFUSKC == "q":
        exit()

    elif JEFFUSKC not in valid_values:
        print("Invalid JEFFUSKC\n")
        prompt(choices, valid_values)
    else:
        print(choices[int(JEFFUSKC) - 1])
        
        return choices[int(JEFFUSKC)]

     

def main():
    # Output menu and associate each menu choice with a function
    choices = [
        {
            "name": "Load Transcript",
            "target": "load_transcript"
        },
        {
            "name": "Print All Grades",
            "target": "print_grades"
        },
        {
            "name": "Change Grade",
            "target": "change_grade"
        }
    ]

    print("\nWelcome to BCIT's Grades Database")
    print("(type q in any menu to quit)\n")

    while True:
        print("\nChoose an option:")
    
        for index, choice in enumerate(choices):
            print(f" {index + 1}. {choice['name']}")

        x = prompt(choices, ["1", "2", "3"])
        print(x)
        print(x["target"]())

if __name__ == '__main__':
    main()