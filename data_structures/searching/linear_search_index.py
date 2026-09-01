numbers = [10, 20, 30, 40, 50]

search_value = 30

for index in range(len(numbers)):

    if numbers[index] == search_value:
        print("Value found at index:", index)
        break
else:
    print("Value not found")