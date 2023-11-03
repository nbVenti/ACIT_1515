empty_set = {}

dog ={
    "name": "Charlie",
    "age": 12,
}

print(dog["name"])
print(dog["age"])

dog["name"] = "Chunk"

for key, value in dog.items():
    print(f"{key}: {value}")

# for key in dog.keys():
# for value in dog.values():
