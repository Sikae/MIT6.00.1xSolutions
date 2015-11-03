__author__ = 'm'

"""
This program calculates the minimum fixed monthly payment needed in order to
pay off a credit card balance within 12 months.
"""


def compute_fixed_monthly_payment(balance, annual_interest_rate):
    pass


def main():
    balance = eval(input("Enter the initial balance: "))
    annual_interest_rate = eval(input("Enter the annual interest rate as a decimal: "))
    lowest_payment = compute_fixed_monthly_payment(balance, annual_interest_rate)

    print("Lowest Payment: " + str(round(lowest_payment, 2)))


if __name__ == "__main__":
    main()
