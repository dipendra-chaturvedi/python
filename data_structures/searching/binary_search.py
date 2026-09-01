numbers = [10, 20, 30, 40, 50, 60, 70]

search_value = 50

low = 0
high = len(numbers) - 1

while low <= high:

    middle = (low + high) // 2

    if numbers[middle] == search_value:
        print("Value found at index:", middle)
        break

    elif numbers[middle] < search_value:
        low = middle + 1

    else:
        high = middle - 1

else:
    print("Value not found")