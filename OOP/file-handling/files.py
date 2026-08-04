import os

files = os.listdir()

for file in files:
    if file.endswith(".txt"):
        print(file)


print(__file__)
print(os.path.dirname(__file__))