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
    transcript = []
    transcript_dir = Path("Assignment_2/transcripts")
    if not transcript_dir.exists():
        sys.exit()

    for i in transcript_dir.iterdir():
        with open(i, "r") as f:
            transcript.append(json.load(f))
    
    return transcript

def load_transcript():
    """
    load_transcript() is responsible for finding and returning a single transcript. It must:

    1. Call load_transcripts() and store the returned list in a variable

    2. Check if the return value of load_transcripts() is None. If so, immediately exit the script
    
    3. Print a message saying "Please choose one of the following transcripts:", then loop through the list of transcripts
        and print each transcript in the format:
        1. firstname lastname (where firstname and lastname are the actual names from the JSON object)
        2. firstname lastname

    4. Call the prompt() function, passing the list and the valid values ["1", "2", "3", "4"]

    5. From the transcript returned by prompt(), print the firstname and lastname, followed by grades for each course

    """
    transcript = load_transcripts()
    if transcript == None:
        sys.exit()

    else:
        print("Please choose one of the following transcripts:")
        for i in transcript:
            print(str(transcript.index(i)+1)+".",i["firstname"], i["lastname"])
        choice = prompt(transcript, ["1", "2", "3", "4"])
        print(choice["firstname"], choice["lastname"])
        for i in range(len(choice["grades"])):
            print(":",choice["grades"][i])
    


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
    transcript = load_transcripts()
    if transcript == None:
        sys.exit()
    else:
        for i in transcript:
            print(i["firstname"], i["lastname"])
            for u in range(len(i["grades"])):
                print(i["grades"][u]["course"], i["grades"][u]["grade"])
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
    

def prompt(choices, valid_values):
    choice = input(">> ")

    if choice == "q":
        sys.exit()

    if choice not in valid_values:
        print("Invalid choice\n")
        return prompt(choices, valid_values)
    else:
        if type(choice) == str:
            choice = int(choice)
            return choices[choice - 1]
        return choices[(choice) - 1]
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
        choice['target']()

if __name__ == '__main__':
    main()