__author__ = 'm'

"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance, and print to screen something of
the format:

Month: 1
Minimum monthly payment: 96.0
Remaining balance: 4784.0
Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of

Remaining balance: 813.4141998135
Finally, print out the total amount paid that year and the remaining balance at the end of the year in the format:

Total paid: 96.0
Remaining balance: 4784.0
"""


def compute_balance(unpaid_balance):
    return unpaid_balance * (1 + 2)


def print_monthly_balance():
    for month in range(12):
        print("This month you have to pay " + str(compute_balance()))
