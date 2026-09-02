def quick_sort(numbers):

    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]

    left = [x for x in numbers[1:] if x <= pivot]
    right = [x for x in numbers[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


numbers = [5, 2, 8, 1, 3]

print(quick_sort(numbers))