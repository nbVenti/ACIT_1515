import requests
import json
from pathlib import Path

path = Path("./Wek113131/words")
path.mkdir(exist_ok=True)

def mock():
    return [{ "meanings": [{ "definitions": [{ "definition": "Definition not found, sorry" }] }] }] 

response = requests.get("https://random-word-api.herokuapp.com/word")

if response.status_code == 200:
    word = response.json()[0]
    file = path / f"{word}.txt"
    file.touch()
    requests = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if requests.status_code == 200:
        data = requests.json()
    else:
        data = mock()
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

print(word,data) 

filenames = []

for i in path.iterdir():
    filenames.append(i.stem)

# print(filenames)

for index, filename in enumerate(filenames):
    print(f"{index + 1}. {filename}")

choice = int(input("\n>>"))

with open(f"./Wek113131/words/{filenames[choice - 1]}.txt") as file:
    print(file.read())
    data = json(file)
    print(data)
    json.loads()
    # print(data[0]["word"])
    # print(data[0]["meanings"][0]["definitions"][0]["definition"])




