"""

Assignment 2: Grades 'Database'
-------------------------------

Assignment 2 is designed to test your understanding of the skills practiced in weeks 5 through 8:
- writing functions
- dictionaries
- converting to and from JSON
- navigating the filesystem
- reading and writing files

For assignment 2 you will be writing a script that loads 'transcripts' (files containing JSON objects with courses and associated grades) and allows you to:
    a). View an individual transcript
    b). Print all transcripts
    c). Change grades in a transcript (i.e. update and save changes to a file)

Notes on implementation are located below inside the functions

"""

from pathlib import Path
import json
import sys
import os

def load_transcripts():
    """
    load_transcripts() is a helper function (that will be called by load_transcript, print_grades, and change_grade). It must:

    1. Create an empty list to hold the transcripts ('transcripts' are JSON objects that will be read from files)
    

    2. Use Path to open the ./transcripts folder
    
    3. Check if the path exists:
        If the path does not exist, the script must immediately exit (using sys.exit() or any other means)
        Else you must iterate through the ./transcripts folder, load the JSON and append it to your list

    4. If your list from step 1 is not empty, return it, otherwise return None

    """
    transcripts = {}
    if not (Path("Assignment_2/transcripts").exists()):
        sys.exit()
    else:
        for i in os.listdir("Assignment_2/transcripts"):
            if i.endswith(".json"):
                with open(f"Assignment_2/transcripts/{i}", 'r') as f:
                    transcripts[i] = json.load(f)


    """
    for i in transcripts_dir.iterdir():
            with open(i, "r") as f:
                transcripts[] = (json.load(f))
    """

              
    
    if transcripts != None:
        return transcripts

def load_transcript():
    """
    load_transcript() is responsible for finding and returning a single transcript. It must:


    1. Call load_transcripts() and store the returned list in a variable

    2. Check if the return value of load_transcripts() is None. If so, immediately exit the script
    
    3. Print a message saying "Please choose one of the following transcripts:", then loop through the list of transcripts
        and print each transcript in the format:
        1. firstname lastname (where firstname and lastname are the actual names from the JSON object)
        2. firstname lastname
`
    4. Call the prompt() function, passing the list and the valid values ["1", "2", "3", "4"]

    5. From the transcript returned by prompt(), print the firstname and lastname, followed by grades for each course

    """
    transcript = load_transcripts()
    if transcript == None:
        sys.exit()
    print("Please choose one of the following transcripts:")
    index = 1
    for i in ((transcript)):
        print(str(index)+":",transcript[i]["firstname"], transcript[i]["lastname"])
        index += 1
    Names = ["Ayesha", "Chris","Jeremy", "Tim"]

    x = prompt(Names, ["1", "2", "3", "4"])
    
    
    for i in transcript:
        if transcript[i]["firstname"] == x:
            print(transcript[i]["firstname"], transcript[i]["lastname"])
            for u in range(len(transcript[i]["grades"])):
                print(transcript[i]["grades"][u])
            print()      

    


def print_grades():
    """
    print_grades() is responsible for printing all transcripts. It must:

    1. Call load_transcripts() and store the returned list in a variable

    2. Check if the return value of load_transcripts() is None. If so, immediately exit the script
    
    3. Loop through the list, printing the firstname and lastname of the transcript followed by all the grades, e.g.:
        Chris Harris
        ACIT 1515: 55
        ACIT 1630: 65
        MATH 1310: 60

        Jeremy Holman
        ACIT 1515: 80
        
        etc.

    """

    grades = load_transcripts()
    if grades == None:
        sys.exit()
    for i in grades:
        print(grades[i]["firstname"],grades[i]["lastname"]+":")
        for u in range(len(grades[i]["grades"])):
            print(grades[i]["grades"][u]['course']+":",grades[i]["grades"][u]['grade'])
        print()
    

def change_grade():
    """
    change_grade() is responsible for finding a single transcript, updating the grade for a single course and writing
    those changes back to the file. It must:

    1. Call load_transcripts() and store the returned list in a variable

    2. Check if the return value of load_transcripts() is None. If so, immediately exit the script
    
    3. Print a message saying "Whose transcript would you like to change?:", then loop through the list of transcripts
        and print each transcript in the format:
        1. firstname lastname (where firstname and lastname are the actual names from the JSON object)
        2. firstname lastname

    4. Call the prompt() function, passing the list and the valid values ["1", "2", "3", "4"]

    5. Print a message saying "Which grade would you like to change?:", then loop through the grades and print each course/grade pair in the format:
        1. ACIT 1515
        2. ACIT 1630
        etc.

    6. Call the prompt() function, passing in just the list of grades from the chosen transcript, and the valid values ["1", "2", "3"]

    7. Print a message saying "Please enter the new grade:", then call input() and allow the user to enter a new grade (validation is optional)

    8. Take the value entered by the user and update the dictionary returned from step 6

    9. Open the file associated with the chosen transcript and dump the updated dictionary to the file, overwriting the previous data

    """
    transcript = load_transcripts()
    if transcript == None:
        sys.exit()
    print("Whos transcript would you like to change?:")
    index = 1
    for i in (transcript):
        print(str(index)+":",transcript[i]["firstname"], transcript[i]["lastname"])
        index += 1
    Names = ["Ayesha", "Chris","Jeremy", "Tim"]

    x = prompt(Names, ["1", "2", "3", "4"])
    u = 0

    for i in transcript:
        if transcript[i]["firstname"] == x:
            print(transcript[i]["firstname"], transcript[i]["lastname"])
            index2 = 1
            for p in range(len(transcript[i]["grades"])):
                print(str(index2)+":",str(transcript[i]["grades"][p]["course"])+":",transcript[i]["grades"][p]["grade"])
                index2 += 1
            u = transcript[i]

    print("Which grade would you like to change?:")
    y = prompt(u["grades"], ["1","2","3"])

    vaild = False
    while vaild == False:
        monkey = input(f"Please enter new grade for the course {y['course']}\n>>")
        if monkey == "q":
            sys.exit()

        elif monkey.isdigit():
            monkey = int(monkey)
            if monkey > 0 and monkey < 100:
                vaild = True
            else:
                print("Invalid input\n")
        else:
            print("Invalid input\n")

    # try monkey.isdidgit() == True and monkey > 0 and monkey < 100:
    # monkey = int(monkey))
    # vaild = True
    # except ValueError:      
    #    print("Invalid input\n")      
    # y = transcript[i]
    ### enter validaion here
    """    
    
    """
    y['grade'] = monkey
    # for i in transcript:
    #     if transcript[i]["firstname"] == x:
    #         for j in range(len(transcript[i]["grades"])):
    #             if transcript[i]["grades"][j]['course'] == y['course']:        
    #                 print(transcript[i]["grades"][j])
    #                 y["grades"] = monkey
    #                 print(transcript[i]["grades"][j])
    #                 break
            
            # print(transcript[i]["grades"](y["grade"]))

    for i in os.listdir("Assignment_2/transcripts"):
        if i.__contains__(x):
            with open(f"Assignment_2/transcripts/{i}", 'w') as f:
                json.dump(transcript[i], f)
    
            # q = Path("Assignment_2, ")
            # with open
    

    

    

    

def prompt(choices, valid_values):
    choice = input(">> ")
   
    if choice == "q":
        sys.exit()

    elif choice not in valid_values:
        print("Invalid choice\n")
        return prompt(((((((((((((((((((((((choices, valid_values)))))))))))))))))))))))

    else:
        if type(choice) == str:
            choice = int(choice)
            return choices[choice - 1]
        return choices[(choice) - 1]
    try:
        choice = int(choice, 10)
        return choices[choice - 1]['target']
    except ValueError:
        print(choice)
        print("Invalid choice\n")
        return prompt(choices, valid_values)
    print(choices[(int(choice)) - 1],"Print return statment, past if statement")
    return choices[(int(choice)) - 1]
    
     

def main():
    # Output menu and associate each menu choice with a function
    choices = [
        {
            "name": "Load Transcript",
            "target": load_transcript
        },
        {
            "name": "Print All Grades",
            "target": print_grades
        },
        {
            "name": "Change Grade",
            "target": change_grade
        }
    ]

    print("\nWelcome to BCIT's Grades Database")
    print("(type q in any menu to quit)\n")

    while True:
        print("\nChoose an option:")
    
        for index, choice in enumerate(choices):
            print(f" {index + 1}. {choice['name']}")

        choice = prompt(choices, ["1", "2", "3"])
        choice["target"]()

if __name__ == '__main__':
    main()