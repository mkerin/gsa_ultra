# Please write your code inside the function stub below.

def solution(n):
    n_yes = 0
    
    # a contains 4 unique values
    n_yes += permute(n, 4)
    
    # a contains 3 unique values
    n_yes += 3 * permute(n, 3)

    # a contains 2 unique values
    n_yes += 3 * permute(n, 2)

    # a contains only 1 unique valueß
    n_yes += permute(n, 1)
    return n_yes

def permute(n, k):
    """
    Niave implementation of nPk = n! // k!
    Fine given that k <= 4.
    """
    res = 1
    for x in range(n-k+1, n+1):
        res *= x
    return res
