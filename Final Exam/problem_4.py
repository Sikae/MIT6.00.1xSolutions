#! python3


def get_sublists(L, n):
    list_of_lists = []
    for i in range(len(L) - n + 1):
        list_of_lists.append(L[i:i + n])

    return list_of_lists


L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n = 4
print(get_sublists(L, n))
