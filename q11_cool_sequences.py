# Please write your code inside the function stub below.
import math


def solution(n):
    """
    Hypothesis:
    Original cool sequence contains
    x, 4 * x, 16 * x, ...
    for odd x.
    
    We can then perform swaps
    eg. x -> 2x where 4x > n
       (and hence not in sequence)
    eg. 4x -> 8x where 16x > n
    etc
    """
    L = gen_L(n)
    swaps = compute_swaps(n)
    W = 2 ** swaps
    return str(L) + str(W)


def gen_L(n):
    """Return L = length of the longest 'cool sequence' from {1,..,n}."""
    # find greatest even power of 2 <= n
    M = int(math.log(n, 2))
    M -= (M % 2)
    L = 0
    
    # How many odd multiples of 2 ** m are there <= n?
    for m in range(0, M+2, 2):
        multiples = n // (2 ** m)
        L += multiples // 2 + multiples % 2
    return L


def compute_swaps(n):
    """
    Compute number of elements, or groups of elements, that we can swap
    whilst not breaking 'cool sequence' properties.
    """
    # max power of 2
    M = int(math.log(n, 2))
    M -= (M % 2) # greatest even
    swaps = 0

    # 1-1 swaps for x -> 2x. eg. 11 -> 22, 13 -> 26
    for m in range(0, M+2, 2):
        swaps += (greatest_odd(n // 2 ** (m+1)) -
                  greatest_odd(n // 2 ** (m+2))) / 2

    # unit swaps eg. 1, 4, 16 -> 2, 8, 32
    # 1. consider odd numbers v up to some sensible range.
    # 2. take the highest even power of 2 st
    #    X := v * 2 ** pow <= n
    # 3. if X <= n // 2 then a unit swap is viable
    lim = (n // 8) + (n // 4) % 2
    for v in range(1, lim + 1, 2):
        highest_pow = int(math.log(n // v, 2))
        highest_pow -= highest_pow % 2
        if 2 * v * 2 ** highest_pow <= n:
            swaps += 1
    return swaps


def greatest_odd(v):
    """Returns greatest odd <= v, st odd > 0."""
    if v % 2 == 0:
        v -= 1
    if v < 0:
        v = 1
    return v


if __name__ == '__main__':
    print(solution(36))
