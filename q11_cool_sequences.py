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
    # max power of 2
    M = int(math.log(n, 2))
    M -= (M % 2) # greatest even
    L = 0
    for m in range(0, M, 2):
        L += n // (2 ** (m+1))
    
    # Original cool seq
    W = 1
    
    # 1-1 swaps for x -> 2x
    W += (godd(n // 2) - godd(n // 4)) / 2

    # 1-1 swaps for 4x -> 8x
    W += (godd(n // 8) - godd(n // 16)) / 2
    return str(L) + str(W)


def godd(v):
    # returns greatest odd <= v
    if v % 2 == 0:
        v -= 1
    return v


if __name__ == '__main__':
    print(solution(36))
