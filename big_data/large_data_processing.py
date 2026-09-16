def read_records():
    for number in range(1, 1000001):
        yield number


total = 0

for record in read_records():
    total += record
    # print(total)  

print("Total:", total)