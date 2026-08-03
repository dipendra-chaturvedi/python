# Create a Set
fruits = {"Apple", "Mango"}
print(fruits)

# Duplicate Values
numbers = {10, 20, 20, 30, 30, 40}
print(numbers)

# Add an Item
fruits = {"Apple", "Mango"}
fruits.add("Banana")
print(fruits)

# Remove an Item
fruits = {"Apple", "Mango", "Banana"}
fruits.remove("Mango")
print(fruits)

# Loop Through a Set
fruits = {"Apple", "Mango", "Banana"}
for fruit in fruits:
    print(fruit)

# Real-Life Example
emails = {
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com"
}

print(emails)

# Can we access a Set using an index?
# No
# print(fruits[0])