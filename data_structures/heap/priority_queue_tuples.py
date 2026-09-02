import heapq

tasks = []

heapq.heappush(tasks, (2, "Database backup"))
heapq.heappush(tasks, (1, "Server failure"))
heapq.heappush(tasks, (3, "Log cleanup"))

while tasks:
    priority, task = heapq.heappop(tasks)
    print(priority, task)