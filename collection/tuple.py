# Tuple = Cannot change (Immutable)
fruits = ("Apple", "Mango", "Banana")

print(fruits)
print(fruits[0])

# Tuple = Cannot change (Immutable)
# fruits[1] = "Orange" 

numbers = (10, 20, 20, 30)

print(numbers.count(20))

print(fruits.index("Mango"))

# Tuple Unpacking
person = ("Dipendra", 25, "Python")

name, age, skill = person

print(name)
print(age)
print(skill)