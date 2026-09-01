numbers = [10, 20, 30, 40, 50]

search_value = 30
index_value = numbers.index(search_value)

for number in numbers:

    if number == search_value:
        
        print("Value found")
        print(f"Index: {index_value}")
        print(f"Value: {search_value}")

        break
else:
    print("Value not found")