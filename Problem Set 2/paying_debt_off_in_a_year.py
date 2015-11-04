__author__ = 'm'

"""
This program calculates the minimum fixed monthly payment needed in order to
pay off a credit card balance within 12 months.
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
