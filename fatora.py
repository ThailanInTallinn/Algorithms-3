import math


def factor(n, low=2):
    if (n == low):
        print(n)
        return n
    elif n <= 0:
        print(0)
        return 0
    elif (n == 1):
        print(1)
        return 1
    elif (low <= 1):
        print(1)
        low += 1

    
    if(n % low == 0):
        print(int(low))
        return factor(int(n / low), low)
    else:
        new_factor = get_factor(n, low + 1)
        if(new_factor == n):
            print(n)
            return n
        print(n // new_factor)
        return factor((n // new_factor), new_factor)


def get_factor(n, curr_low):
    for i in range(curr_low, math.isqrt(n) + 1):
        if(n % i == 0):
            return i
    return n


factor(36, 1)

