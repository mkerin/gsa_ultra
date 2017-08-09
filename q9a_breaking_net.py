# Please write your code inside the function stub below.
MOD = 10 ** 9 + 7


def solution(n):
    """
    Recursive solution?
    See project euler Q on coin combinations
    """
    return my_func(n, 4)

def my_func(new_sum, throw_score):
    """
    Recursive function to compute no. of combinations
    of throws that add up to make new_sum.
    
    Can think of this as traversing down a k-ary tree,
    where k is the number of different throw scores,
    with a level for each throw.
    """
    if throw_score == 2:
        # at bottom node of tree -> count leaves
        # ie no. of ways to sum to new_sum with
        # 2- or 1-point throws
        return new_sum // 2 + 1
    else:
        res = 0
        while new_sum >= 0:
            res += my_func(new_sum, throw_score - 1)
            new_sum -= throw_score
        res %= MOD
        return res
