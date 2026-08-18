name = input("Enter name: ")
age = input("Enter age: ")

if not name.strip():
    print("Name cannot be empty")

elif not age.isdigit():
    print("Age must be a number")

elif int(age) < 18:
    print("Age must be 18 or above")

else:
    print("Input is valid")
