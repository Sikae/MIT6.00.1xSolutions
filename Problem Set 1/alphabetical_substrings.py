__author__ = 'm'

"""
This program prints the longest substring of a string in which the letters occur in alphabetical order.
Assume s is a string of lower case characters. For example, if s = 'azcbobobegghakl', then the program prints

Longest substring in alphabetical order is: beggh
"""


def obtain_longest_substring(string):
    current_substring = longest_substring = string[0]
    for letter in string[1:]:
        if letter >= current_substring[-1]:
            current_substring += letter
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
        else:
            current_substring = letter
    return longest_substring


def main():
    s = input("Enter a string: ")
    print("Longest substring in alphabetical order is: " + obtain_longest_substring(s))

if __name__ == "__main__":
    main()
