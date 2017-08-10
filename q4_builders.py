# Please write your code inside the function stub below.
import itertools as it
from fractions import gcd


def solution(n, m, d):
    """
    Analytical solution;
    Simply move nail from min gap to middle of max gap.
    """
    offset_l = [0] + list(d)
    offset_r = list(d) + [n]
    diffs = [x-y for x, y in it.izip(offset_r, offset_l)]
    
    # Find index of the two gaps to be merged.
    # Search a moving window width 2 for the smallest sum.
    # j'th window implies merging diff j + diff j+1
    L = len(diffs)
    win_w2 = [x+y for x, y in it.izip(diffs[:L-1], diffs[1:])]
    j = win_w2.index(min(win_w2))
    
    # find index of maximum gap (ie the one we'll split in 2)
    k = max(diffs)
    
    # Forming an irreducible fraction
    numerator = k // 2 * (k // 2 + k % 2) * min(win_w2)
    denom = diffs[j] * diffs[j+1] * k
    gg = gcd(numerator, denom)
    numerator /= gg
    denom /= gg
    return str(numerator) + str(denom)


if __name__ == '__main__':
    D = []
    with open('input/q4_input.txt') as f:
        n, m = f.readline().rstrip("\n").split()
        n, m = int(n), int(m)
        D = tuple(int(x) for x in f.readline().split())
    print(n, m)
    print(len(D))
    res = solution(n, m, D)
    print(res)
