x = input("first Number\n>>")
y = input("second Number\n>>")

try:
    x = int(x)
    y = int(y)
    (x+y)
    (x-y)
    (x*y)
    (x/y)
except ValueError:
    print("Enter Numbers")
except ZeroDivisionError:
    print("make second number not zero")
else:
    print((x+y),
    (x-y),
    (x*y),
    (x/y))