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


