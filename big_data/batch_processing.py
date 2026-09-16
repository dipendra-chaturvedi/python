orders = [100, 200, 150, 300, 250, 400]

batch_size = 2

for i in range(0, len(orders), batch_size):

    batch = orders[i:i + batch_size]

    print("Processing:", batch)