import json
from flask import Flask

app = Flask(__name__)

@app.route("/words/<length>")
def get_words(length):
    """
    open the file associated with the length, i.e. if length is 5, open './words/5-letter-words.json'
    load the json from the file and return it
    """
    with open(f'lab 7/words/{length}-letter-words.json') as f:
        r = json.load(f)
    return r
    
    # return f"<h1>Your word is {length} letters long </h1>" # change or remove this line



if __name__ == "__main__":
    app.run()