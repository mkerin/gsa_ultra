# Please write your code inside the function stub below.
import itertools as it
from fractions import gcd

def solution(n, m, d):
    """
    Attempt at analytical solution
    Simply move nail from min gap to
    middle of max gap.
    """
    # DP: num of nails?
    offset_l = [0] + list(d)
    offset_r = list(d) + [n]
    diffs = [x-y for x, y in it.izip(offset_r, offset_l)]
    prod = CalcProd(diffs)

    # Find index of diffs that we'll merge..
    # moving window width 2 with smallest sum...
    # j'th window implies merging diff j + diff j+1
    L = len(diffs)
    win_w2 = [x+y for x, y in it.izip(diffs[:L-1], diffs[1:])]
    j = win_w2.index(min(win_w2))
    print(prod)
    
    # find index of diffs that we'll split
    # ie the max diff
    # 5 -> 3, 2
    # 4 -> 2, 2
    k = max(diffs)
    print("max diffs: {}".format(k))
    print("max loc: {}".format(diffs.index(max(diffs))))
    print("min win_w2 {} from {}, {}".format(min(win_w2), diffs[j], diffs[j+1]))
    
    numerator = k // 2 * (k // 2 + k % 2) * min(win_w2)
    denom = diffs[j] * diffs[j+1] * k
    gg = gcd(numerator, denom)
    numerator /= gg
    denom /= gg
    print("gcd: {}".format(gg))
    return str(numerator) + str(denom)


def CalcProd(iterable):
    res = 1
    for x in iterable:
        res *= x
    return res


if __name__ == '__main__':
    D = []
    with open('q4_input.txt') as f:
        n, m = f.readline().rstrip("\n").split()
        n, m = int(n), int(m)
        D = tuple(int(x) for x in f.readline().split())
    print(n, m)
    print(len(D))
    res = solution(n, m, D)
    print(res)
