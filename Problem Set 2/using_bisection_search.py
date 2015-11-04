__author__ = 'm'

"""
This program uses bisection search to find out the smallest monthly payment such that
we can pay off the entire balance within a year.
"""

from paying_debt_off_in_a_year import compute_balance_after_a_year


def compute_initial_lower_and_upper_bounds(balance, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12.0
    lower_bound = balance / 12.0
    upper_bound = balance * (1 + monthly_interest_rate) ** 12 / 12.0

    return lower_bound, upper_bound


def compute_lowest_payment_using_binary_search(balance, annual_interest_rate):
    lower_bound, upper_bound = compute_initial_lower_and_upper_bounds(balance, annual_interest_rate)

    while True:
        lowest_payment = (lower_bound + upper_bound) / 2.0
        balance_after_a_year = compute_balance_after_a_year(balance, lowest_payment, annual_interest_rate)

        if abs(balance_after_a_year) <= 0.01:
            return lowest_payment

        if balance_after_a_year > 0:
            lower_bound = lowest_payment
        else:
            upper_bound = lowest_payment


def main():
    balance = eval(input("Enter the initial balance: "))
    annual_interest_rate = eval(input("Enter the annual interest rate: "))

    lowest_payment = compute_lowest_payment_using_binary_search(balance, annual_interest_rate)
    print("Lowest Payment: " + str(round(lowest_payment, 2)))


if __name__ == "__main__":
    main()
