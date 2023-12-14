import sqlite3

connection = sqlite3.connect('data.db')

"""
Class
"""

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Hi I am", self.name, "and I am", self.age, "years old")
    
    def eat(self, food):
        print(f"{self.name} is Eating {food}")

dog1 = Dog("Tim", 34)
dog1.eat("normal food")
dog1.speak()

dog2 = Dog("Chunk", 12)
dog2.eat("abnormal food")
dog2.speak()