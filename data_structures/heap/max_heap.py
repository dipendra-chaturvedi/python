import heapq

numbers = [5, 2, 8, 1, 3]

max_heap = []

for number in numbers:
    heapq.heappush(max_heap, -number)

largest = -heapq.heappop(max_heap)

print(largest)