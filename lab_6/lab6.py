from pathlib import Path
import json
import re
import sys
 
def main():
    # 1. List all the files and folders in the current directory
    for f in Path.cwd().iterdir():
        print(f)

    

    # 2. Repeat #1, but print a number (starting at zero, not one) before the file/folder name, e.g.
        # 1. /Users/you/BCIT/lab1.py
        # 2. /Users/you/BCIT/lab2.py
    i = 1
    for f in Path.cwd().iterdir():
        u = str(f)
        print(f"{i} {u}")
        i += 1


    # 3. Create a folder in the current directory named assignment2
    new_folder = Path("Lab_6/assignment2")
    if not (new_folder.exists()):
        new_folder.mkdir() 

    # 4. Create a folder inside the assignment2 folder named transcripts
    new_folder = Path("Lab_6/assignment2/transcripts")
    if not (new_folder.exists()):
        new_folder.mkdir()

    # 5. Create four files inside the transcripts directory:
        # Ayesha-Anzer.json
        # Chris-Harris.json
        # Jeremy-Holman.json
        # Tim-Guicherd.json
    transcript = {}
    with open("lab_6/assignment2/transcripts/Ayesha-Anzer.json", 'w') as f:
        json.dump(transcript, f)
    with open("lab_6/assignment2/transcripts/Chris-Harris.json", 'w') as f:
        json.dump(transcript, f)
    with open("lab_6/assignment2/transcripts/Jeremy-Holman.json", 'w') as f:
        json.dump(transcript, f)
    with open("lab_6/assignment2/transcripts/Tim-Guicherd.json", 'w') as f:
        json.dump(transcript, f)
    

    # 6. Copy the following (i.e. copy and paste, not using python) JSON into ./assignment2/transcripts/Chris-Harris.json
    transcript ={
        "firstname": "Chris", 
        "lastname": "Harris", 
        "grades": [
            { "course": "ACIT 1630", "grade": 55 }, 
            { "course": "ACIT 1515", "grade": 45 }, 
            { "course": "MATH 1310", "grade": 50 }
        ]
    }
    with open("lab_6/assignment2/transcripts/Chris-Harris.json", 'w') as f:
        json.dump(transcript, f)

    # 7. Create an empty dictionary
    transcript = {}

    # 8. Use Path and .open() to open ./assignment2/transcripts/Chris-Harris.json, then load the json into the variable from step 7
    x = Path("lab_6/assignment2/transcripts/Chris-Harris.json")
    with open(x, 'r') as f:
        transcript = json.load(f)

    # 9. Using your dictionary from step 7, print all the grades on one line
    print(transcript["grades"])

    # 10. Loop through the grades. If the course is ACIT 1515, change the grade to a passing grade
    for i in transcript["grades"]:
        if i['course'] == "ACIT 1515":
            i["grade"] = '50'


    # 11. Confirm the grade has been updated by printing the variable from step 7
    print((transcript))

    # 12. Write the updated variable to a new file using open(), ./assignment2/transcripts/Chris-Harris-Updated.json
    with open("lab_6/assignment2/transcripts/Chris-Harris-updated.json", 'w') as f:
        json.dump(transcript, f)

if __name__ == '__main__':
    main()