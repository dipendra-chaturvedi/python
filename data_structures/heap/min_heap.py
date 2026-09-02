import heapq

numbers = [5, 2, 8, 1, 3]

heapq.heapify(numbers)

print(numbers)
print(heapq.heappop(numbers))
print(heapq.heappop(numbers))