import os

path = r"C:\Development\python"

print("Current directory:", os.getcwd())
print("Exists:", os.path.exists(path))
print("Is directory:", os.path.isdir(path))
print("Files/Folders:", os.listdir(path))