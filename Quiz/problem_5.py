__author__ = 'm'

def primes_list(N):
    '''
    N: an integer
    '''
    primes = []

    for number in range(2, N + 1):
        is_prime = True
        for factor in range(2, number):
            if number % factor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)

    return primes
