# Problem 2.1
balance = float(input("Enter the outstanding balance on your credit card: "))
annual_interest_rate = float(input("Enter the annual interest rate as a decimal: "))
monthly_payment_rate = float(input("Enter the minimum monthly payment rate as a decimal: "))

months_per_year = 12

monthly_interest_rate = annual_interest_rate / months_per_year

for month in range(12):
  
    minimum_payment = monthly_payment_rate * balance
    unpaid_balance = balance - minimum_payment
    balance = unpaid_balance + (monthly_interest_rate * unpaid_balance)
print("Remaining balance: {:.2f}".format(balance))

#Testcase 2.1
#Enter the outstanding balance on your credit card: 5000.00
#Enter the annual interest rate as a decimal: 0.18
#Enter the minimum monthly payment rate as a decimal: 0.02

#Problem 2.2
