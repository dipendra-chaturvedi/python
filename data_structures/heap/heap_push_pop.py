import heapq

numbers = [2, 5, 8, 3]

heapq.heapify(numbers)
heapq.heappush(numbers, 1)

print(numbers)

smallest = heapq.heappop(numbers)

print(smallest)
print(numbers)