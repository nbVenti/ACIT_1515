# BASICS ------------------------------------------

# create a variable, store a primitive value
x = ""
# create a variable, store a list
y = [1,2,3,4]
# iterate through the list
for i in y:
    print(i)
# update value in the list
y[0] = "test"
# create a variable, store a set
z = {}
# iterate through the set
for i in z:
    print(i)
# convert a list to a set
myList = []
myList = set(myList)
# create a variable, store a dictionary
d = {}
# iterate through keys and values in the dictionary
for i in d:
    for u in range(len(i[d])):
        print(u)
# update value in the dictionary
d["key"] = "test"
# write an if statement that prints a value
if True:
    print("Hello world")
# write an if statement that sets a variable conditionally
b = 1
a = 2
if True:
    a = b
    print(a, "a")
    
# create a function that returns a value
def add(x,y):
    j = int(x) + int(y)
    return j
# call the function and store the returned value
k = add(1,2)
# create a function with a parameter that alters and returns the parameter
def addOne(x):
    x += 1
    return x
# call the function and store the returned value
o = addOne(1)
print(o)

# COMBINATIONS -------------------------------

# create a variable, store a list with dictionaries in it
myListv2 = [{"a": 2,"b":1, "c":3},{"d":5,"e": 10, "f": 88}]

# iterate through the list, print values
for i in myListv2:
    print(i)
# iterate through the list, update a value
for i in (myListv2):
    for u in i:
        i[u] += 1   

print(myListv2)

# create a variable, store a list
myListv3 = ["a","b","c"]
# iterate through the list, passing each value to a function
def printLetter(x):
    print(x)
    
for i in myListv3:
    printLetter(i)


# create a function that conditionally returns a True/False value

def ifTrue(x):
    if x == True:
        return True
    else:
        return False

# call the function and use the result in an if statement
x = False
if ifTrue(x):
    print("x","True")
else:
    print("x","False")
