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


def compute_updated_balance(balance, minimum_monthly_payment, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12.0
    monthly_unpaid_balance = balance - minimum_monthly_payment

    return monthly_unpaid_balance * (1 + monthly_interest_rate)


def compute_minimum_monthly_payment(monthly_payment_rate, balance):
    return monthly_payment_rate * balance


def round_number_two_decimals(number):
    return round(number, 2)


def get_updated_balance_and_minimum_monthly_payment(balance, annual_interest_rate, monthly_payment_rate):
    minimum_monthly_payment = compute_minimum_monthly_payment(monthly_payment_rate, balance)
    updated_balance = compute_updated_balance(balance, minimum_monthly_payment, annual_interest_rate)

    return updated_balance, minimum_monthly_payment


def print_monthly_balance(balance, annual_interest_rate, monthly_payment_rate, month):
    updated_balance, minimum_monthly_payment = get_updated_balance_and_minimum_monthly_payment(balance,
                                                                                               annual_interest_rate,
                                                                                               monthly_payment_rate)
    print("Month: " + str(month))
    print("Minimum monthly payment: " + str(round_number_two_decimals(minimum_monthly_payment)))
    print("Remaining balance: " + str(round_number_two_decimals(updated_balance)))


def print_balance_after_a_year(balance, annual_interest_rate, monthly_payment_rate):
    total_paid = 0
    for month in range(12):
        print_monthly_balance(balance, annual_interest_rate, monthly_payment_rate, month + 1)
        balance, monthly_payment = get_updated_balance_and_minimum_monthly_payment(balance, annual_interest_rate,
                                                                                   monthly_payment_rate)
        total_paid += monthly_payment

    print("Total paid: " + str(round_number_two_decimals(total_paid)))
    print("Remaining balance: " + str(round_number_two_decimals(balance)))


def main():
    balance = eval(input("Enter the initial balance: "))
    annual_interest_rate = eval(input("Enter the annual interest rate as a decimal: "))
    monthly_payment_rate = eval(input("Enter the minimum monthly payment rate as a decimal: "))

    print_balance_after_a_year(balance, annual_interest_rate, monthly_payment_rate)


if __name__ == "__main__":
    main()
