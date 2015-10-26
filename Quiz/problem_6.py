__author__ = 'm'


def count7(N):
    """
    N: a non-negative integer
    """
    if N == 0:
        return 0

    return int(N % 10 == 7) + count7(N // 10)
