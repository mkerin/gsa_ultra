# Please write your code inside the function stub below.


def solution(n):
    n_yes = 0
    
    # 4 unique values
    n_yes += Permute(n, 4)
    
    # 3 unique values
    # * which value to replicate
    # * ways to place replicated value
    n_yes += Permute(n, 3) * 3 * 1
    
    # 2 unique values
    # * which value to replicate
    # * ways to place replicated value
    n_yes += Permute(n, 2) * 2 * 3
    
    # a contains only 1 unique value
    n_yes += Permute(n, 1)
    return n_yes


def Permute(n, k):
    """
    Niave implementation of nPk = n! // k!
    Fine given that k <= 4.
    """
    if n < k:
        return 0
    res = 1
    for x in range(n-k+1, n+1):
        res *= x
    return res


if __name__ == '__main__':
    res = solution(3)
    print(res)
