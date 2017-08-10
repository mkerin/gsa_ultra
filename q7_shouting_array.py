# Please write your code inside the function stub below.


def solution(n):
    n_yes = 0
    
    # 4 unique values in a.
    n_yes += nPk(n, 4)
    
    # 2 unique values xy in a.
    # Valid strings: xxxy, xxyx, xyxx, yxxx
    n_yes += nPk(n, 2) * 4
    return n_yes


def nPk(n, k):
    """Niave implementation of nPk = n! // k!. Fine given n, k both small."""
    if n < k:
        return 0
    res = 1
    for x in range(n-k+1, n+1):
        res *= x
    return res
