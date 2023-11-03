from pathlib import Path
import json
import re
import sys
 
def main():
    # 1. List all the files and folders in the current directory

    # 2. Repeat #1, but print a number (starting at zero, not one) before the file/folder name, e.g.
        # 1. /Users/you/BCIT/lab1.py
        # 2. /Users/you/BCIT/lab2.py

    # 3. Create a folder in the current directory named assignment2

    # 4. Create a folder inside the assignment2 folder named transcripts

    # 5. Create four files inside the transcripts directory:
        # Ayesha-Anzer.json
        # Chris-Harris.json
        # Jeremy-Holman.json
        # Tim-Guicherd.json

    # 6. Copy the following (i.e. copy and paste, not using python) JSON into ./assignment2/transcripts/Chris-Harris.json
    {
        "firstname": "Chris", 
        "lastname": "Harris", 
        "grades": [
            { "course": "ACIT 1630", "grade": 55 }, 
            { "course": "ACIT 1515", "grade": 45 }, 
            { "course": "MATH 1310", "grade": 50 }
        ]
    }

    # 7. Create an empty dictionary

    # 8. Use Path and .open() to open ./assignment2/transcripts/Chris-Harris.json, then load the json into the variable from step 7

    # 9. Using your dictionary from step 7, print all the grades on one line

    # 10. Loop through the grades. If the course is ACIT 1515, change the grade to a passing grade

    # 11. Confirm the grade has been updated by printing the variable from step 7

    # 12. Write the updated variable to a new file using open(), ./assignment2/transcripts/Chris-Harris-Updated.json

if __name__ == '__main__':
    main()