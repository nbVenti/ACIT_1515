import requests
import flask

reponse = requests.get('https://jsonplaceholder.typicode.com/users')

print(reponse) # <Response [200]>
print(reponse.status_code, type(reponse.status_code)) # 200 <class 'int'>  

data = reponse.json() # convrt to json format

print(data, type(data)) # <class 'list'>

user = data[0]
print(user["email"], user['name'] , user['address']['zipcode']) #


res = requests.get('http://127.0.0.1:5000/')
data = res.json