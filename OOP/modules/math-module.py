import math

loan_amount = 500000
annual_interest = 8.5
years = 5

monthly_interest = annual_interest / (12 * 100)
months = years * 12

emi = (
    loan_amount
    * monthly_interest
    * math.pow(1 + monthly_interest, months)
) / (
    math.pow(1 + monthly_interest, months) - 1
)

total_payment = emi * months
total_interest = total_payment - loan_amount

print(f"Monthly EMI: ₹{round(emi, 2)}")
print(f"Total Interest: ₹{round(total_interest, 2)}")
print(f"Total Payment: ₹{round(total_payment, 2)}")