__author__ = 'm'

"""
This program prints the number of vowels (lowercase) contained in a string. It is assumed string is a string of lower
case characters. For example, if string = 'azcbobobegghakl', the program prints:

Number of vowels: 5
"""


def count_vowels(string):
    counter = 0
    for letter in string:
        if letter in "aeiou":
            counter += 1
    return counter


def main():
    s = input("Enter a string: ")
    print("Number of vowels: " + str(count_vowels(s)))


if __name__ == "__main__":
    main()
