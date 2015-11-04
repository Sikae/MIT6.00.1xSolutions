#! python3


def get_sub_lists(L, n):
    list_of_lists = []
    for i in range(len(L) - n + 1):
        list_of_lists.append(L[i:i + n])

    return list_of_lists


def longest_run(L):
    current_list = longest_ascending_list = [L[0]]

    for e in L[1:]:
        if current_list[-1] <= e:
            current_list.append(e)
            if len(current_list) > len(longest_ascending_list):
                longest_ascending_list = current_list
        else:
            current_list = [e]

    return len(longest_ascending_list)
