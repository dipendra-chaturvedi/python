import heapq

numbers = [10, 4, 7, 20, 15, 3]

# Min Heap
min_heap = numbers.copy()
heapq.heapify(min_heap)

print("Min:", heapq.heappop(min_heap))


# Max Heap
max_heap = []

for number in numbers:
    heapq.heappush(max_heap, -number)

print("Max:", -heapq.heappop(max_heap))