import heapq

tickets = []

heapq.heappush(tickets, (3, "Password reset"))
heapq.heappush(tickets, (1, "Production server down"))
heapq.heappush(tickets, (2, "Payment failure"))

while tickets:

    priority, ticket = heapq.heappop(tickets)

    print("Handling:", ticket)