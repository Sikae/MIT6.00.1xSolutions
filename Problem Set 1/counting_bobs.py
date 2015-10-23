__author__ = 'm'

"""
This program prints the number of times the string "bob" occurs in a string.
Assume s is a string of lower case characters. For example, if string = 'azcbobobegghakl', then the program prints:

Number of times bob occurs is: 2
"""


def count_bobs(string):
    keyword = "bob"
    keyword_length = len(keyword)
    counter = 0
    for index in range(len(string) - keyword_length + 1):
        if string[index:index + keyword_length] == keyword:
            counter += 1
    return counter


def main():
    s = input("Enter a string: ")
    print("Number of times bob occurs is: " + str(count_bobs(s)))


if __name__ == "__main__":
    main()
