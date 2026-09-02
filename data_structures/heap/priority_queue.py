import heapq

tickets = []

heapq.heappush(tickets, (2, "Login issue"))
heapq.heappush(tickets, (1, "Server down"))
heapq.heappush(tickets, (3, "General question"))

while tickets:
    priority, ticket = heapq.heappop(tickets)
    print(priority, ticket)