import json

transcript = {
    "firstname": "Chris",
    "lastname": "Harris",
    "grades":[
        {"ACIT 1515": "100"},
        {"ACIT 1630": "65"},
    ]
}

with open('week 9/transcript.json', 'w') as f:
    json.dump(transcript, f)

with open('week 9/transcript.json', 'r') as f:
    transcript = json.load(f)


