try:
    account_balance = 5000

    withdraw_amount = int(input("Enter withdrawal amount: "))

    if withdraw_amount > account_balance:
        raise ValueError("Insufficient Balance")

    account_balance -= withdraw_amount

    print("Transaction Successful")
    print("Remaining Balance:", account_balance)

except ValueError as e:
    print("Transaction Failed:", e)

finally:
    print("Thank you for banking with us.")