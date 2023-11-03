"""
This code demonstrates the usage of dictionaries and pathlib module in Python.
It creates an empty dictionary and a dictionary with some key-value pairs.
It also shows how to modify the values of a dictionary and iterate over its keys and values.
Additionally, it creates a file and a folder using the pathlib module and prints the contents of the current directory.
"""
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


"""""
Path() - pathlib    
(some of the operations below are also available in the os module with slightly different functionality)
"""""

from pathlib import Path

# We need to create a Path object for any file/foler that we want to navigate or read

# creating a file
"""
./ - current directory
../ - parent directory
../../../ - grandparent director or 3 levels up or go up 3 folders
./folder1/folder2/folder3 - go down 3 folders
"""

new_file = Path("./new_file.txt") # Paths are unix-style but they will worl on any OS

new_file.touch() # creates a new file

new_folder = Path("./new_folder")
new_folder.mkdir() # creates a new folder

new_test_file = Path("./new_folder/test.txt")
new_test_file.touch() # creates a new file


current_dir = Path.cwd() # returns the current directory

for f in current_dir.iterdir():
    print(f, f.is_dir())
    # check if f is a file or a folder f is
    # is_dir() - returns True if f is a folder
    # is_file() - returns True if f is a file

for index, f in enumerate(current_dir.iterdir()):
    print(f"{index + 1}. {f}")

# simple version of reading/writing files
new_test_file.write_text("Hello World!")

contents = new_file.read_text()
print(contents, type(contents))

# more complex version of reading/writing files
with new_test_file.open(mode="w") as file:
    file.write("Hello World!")

"""
'w' = Write mode
'r' = Read mode
'a' = Append mode
'x' = Create mode
"""

file_handle = open(./text.txt, "a")
file_handle.write("Hello World!")
file_handle.close()