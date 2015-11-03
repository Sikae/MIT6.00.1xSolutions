__author__ = 'm'

"""
This program uses bisection search to find out the smallest monthly payment such that
we can pay off the entire balance within a year.
"""


def compute_lowest_payment_using_binary_search(balance, annual_interest_rate):
    pass


def main():
    balance = eval(input("Enter the initial balance: "))
    annual_interest_rate = eval(input("Enter the annual interest rate: "))

    lowest_payment = compute_lowest_payment_using_binary_search(balance, annual_interest_rate)
    print("Lowest Payment: " + str(round(lowest_payment, 2)))


if __name__ == "__main__":
    main()
