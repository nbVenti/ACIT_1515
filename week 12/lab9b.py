class notPas(Exception):
    pass
x = input(" >>\n")
try:
    if int(x) >= 0:
        print("nice")
    else:
        raise notPas
except notPas:
    print("enter positive number")
