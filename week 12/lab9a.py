x = input(" >>File Name\n")
try:
    with open(f"./week 12/{x}",'r') as f:
        print(f.read())
except:
    print("File not found")
