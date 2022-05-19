import os

from pip import main

# uses os.walk() to return a list containing the root, dirs and files, given a search_path
# cycles through files and checks whether one is filename
def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return True
    return False


#def check_test_folder():

pattern = "hello.txt"
path = "/Users/bbsteps/Documents/sara"
if(find_file(pattern, path)):
    print("found it")
else:
    print("not found")
