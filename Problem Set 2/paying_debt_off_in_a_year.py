__author__ = 'm'

"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance
within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is
a constant amount that will be paid each month.
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance
within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is
a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for
example:

Lowest Payment: 180
Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for
that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is
possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is
found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for
example:

Lowest Payment: 180
Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for
that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is
possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math
is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""


def compute_updated_balance(balance, fixed_payment, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12.0
    monthly_unpaid_balance = balance - fixed_payment

    return monthly_unpaid_balance * (1 + monthly_interest_rate)


def compute_balance_after_a_year(balance, fixed_payment, annual_interest_rate):
    for i in range(12):
        balance = compute_updated_balance(balance, fixed_payment, annual_interest_rate)

    return balance


def compute_fixed_monthly_payment(balance, annual_interest_rate):
    fixed_payment = 0

    while True:
        fixed_payment += 10
        balance_after_a_year = compute_balance_after_a_year(balance, fixed_payment, annual_interest_rate)

        if balance_after_a_year <= 0:
            return fixed_payment


def main():
    balance = eval(input("Enter the initial balance: "))
    annual_interest_rate = eval(input("Enter the annual interest rate as a decimal: "))
    lowest_payment = compute_fixed_monthly_payment(balance, annual_interest_rate)

    print("Lowest Payment: " + str(round(lowest_payment, 2)))


if __name__ == "__main__":
    main()
