__author__ = 'm'


def f(s):
    return 'a' in s


def satisfies_f(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    bool_list = []

    for e in L:
        bool_list.append(f(e))

    for i in range(len(bool_list)):
        if not bool_list[i]:
            L[i] = None

    while True:
        try:
            L.remove(None)
        except ValueError:
            break

    return len(L)

L = ['a', 'b', 'a']
print(satisfies_f(L))
print(L)
