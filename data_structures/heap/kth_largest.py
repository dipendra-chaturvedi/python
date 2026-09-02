import heapq

numbers = [10, 4, 7, 20, 15, 3]

k = 2

heap = []

for number in numbers:
    heapq.heappush(heap, number)

    if len(heap) > k:
        heapq.heappop(heap)

print(heap[0])