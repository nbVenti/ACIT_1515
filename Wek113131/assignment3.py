import requests
import json
from pathlib import Path

def mock():
    return [{ "meanings": [{ "definitions": [{ "definition": "Definition not found, sorry" }] }] }]

"""
Part 1: use Path to create a new directory (make sure you are running the script from the same folder that contains the file) named 'words'
"""




"""
Part 2: make a get request to https://random-word-api.herokuapp.com/word

If the status code is 200, extract the word from the http response
and create a .txt file (using Path) with the name you retrieved inside the folder from step 1

For example, if your random word is "produce", you will create a file named produce.txt in the 'words' folder
"""




"""
Part 3: make a get request to https://api.dictionaryapi.dev/api/v2/entries/en/YOUR-WORD, where YOUR-WORD is the word you fetched in the previous step, e.g.: https://api.dictionaryapi.dev/api/v2/entries/en/produce

If the status code is 200, create a variable named data and store the returned json in it
Else, create a variable named data and store the returned value of the mock() function (provided above for you) in it

Next, write the value in the data variable (using json.dump(), NOT json.dumps()) into the file you created in part 2
"""




"""
Part 4: create a list called 'filenames'. 

Iterate through all the files in the words dictionary, appending the file names (use the .name property to access the file name) into your 'filenames' list
"""




"""
Part 5: use enumerate() to print out all the file names in your filenames list, e.g.:

1. pats.txt
2. produce.txt

then use input() to ask the user which word they would like the definition for 

NOTE: assume you are going to get valid input, so int(input("Please enter the word you want the definition for: ")) is OK
"""




"""
Part 6: open the file associated with the user's choice, load the json using json.load() (NOT json.loads()) and print the definition of the word 

IF you store the result of json.load() into a variable named 'data', you could retrieve the definition using:
data[0]["meanings"][0]["definitions"][0]["definition"]
"""
