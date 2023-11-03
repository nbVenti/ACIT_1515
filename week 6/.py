
if __name__ == "__main__":
    #set - List that only contains unique values (no dupe) and is not ordered

    term1 = ["ACIT1515", "ACIT1630", "MATH1310", "ACIT1515"] 
    print(term1)

    # list(), tuple(), set()
    term1 = set(term1)
    print(term1)

    term1 = list(term1)
    print(term1)

    courses = {"ACIT1515", "ACIT1630", "MATH1310", "ACIT1515"}
    print(courses)

    name =  set("Christohper Harris")
    name =  set("Christohper Harris".replace(" ", "".lower()))
    print(name,len(name))


    dog = {
        "name" : "Charlie",
        "age": 12,
        "breed": "Ridgeback"
    }
    print(dog)
    print(dog["name"])
    dog["age"] = 13
    print(dog)

    for key in dog:
        print(key)

    for k in dog.keys():
        print(k)

    for v in dog.values():
        print(v)
    
    for t in dog.items():
        print(t)

    print(f"My dog's name is {dog['name']}")

    # any() - conditional check for a value in a list/set, returns True/False

    name = "Christopher Harris"
    print(name)


    # isupper(), islower(), isdigit()
    # for i in range(len(name)):
    # for charater in name:
    #     if charater.isupper():
    #         print("The name does have an uppercase charater")
    #         break


    if any(charater.isupper() for charater in name):
        print("The name does have an uppercase charater")

    def addNumbers(num1:int, num2:int) -> int:
        print(num1+num2)
        