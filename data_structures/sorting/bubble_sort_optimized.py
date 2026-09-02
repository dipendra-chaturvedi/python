numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):

    swapped = False

    for j in range(len(numbers) - 1 - i):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True

    if not swapped:
        break

print(numbers)