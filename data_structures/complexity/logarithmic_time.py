# O(log n) - Logarithmic Time

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

target = 70

left = 0
right = len(numbers) - 1

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        print("Found:", target)
        break
    elif numbers[middle] < target:
        left = middle + 1
    else:
        right = middle - 1