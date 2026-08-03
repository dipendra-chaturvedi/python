# Create a Dictionary
student = {
    "name": "Dipendra",
    "age": 25,
    "city": "Mumbai"
}

print(student)

# Access Value
student = {
    "name": "Dipendra",
    "age": 25
}

print(student["name"])
print(student["age"])

# Add a New Item
student = {
    "name": "Dipendra"
}

student["city"] = "Mumbai"

print(student)

# Update a Value
student = {
    "name": "Dipendra",
    "age": 25
}

student["age"] = 26

print(student)

# Remove an Item
student = {
    "name": "Dipendra",
    "age": 25
}

student.pop("age")

print(student)

# Loop Through Dictionary
student = {
    "name": "Dipendra",
    "age": 25
}

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, ":", value)

print(len(student))

# Real-Life Example
employee = {
    "id": 101,
    "name": "Dipendra",
    "department": "IT",
    "salary": 60000
}

print(employee)