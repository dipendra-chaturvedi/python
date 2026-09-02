numbers = [5, 2, 8, 1, 3]

for j in range(len(numbers) - 1):

    if numbers[j] > numbers[j + 1]:

        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)