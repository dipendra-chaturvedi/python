balance = 5000
withdraw = 3000

if withdraw <= balance:
    balance -= withdraw
    print("Transaction Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")