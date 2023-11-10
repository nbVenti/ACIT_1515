from flask import Flask
import json

app = Flask(__name__)   

@app.get('/')
def index():
    return "<h1>Hello World</h1>"

@app.get('/course/<name>')
def course(name):
    return f"<h1>Course:{name}</h1>"

@app.get('/word')
def get_word():
    reponses = {}

    with open('week 10/text.json','r') as f:
        reponses = json.load(f)

    return reponses

if __name__ == '__main__':
    app.run()