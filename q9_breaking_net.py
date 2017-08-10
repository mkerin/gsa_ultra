# Please write your code inside the function stub below.

# constants
MOD = 10 ** 9 + 7


def solution(n):
    return find_throw_combos(n, 4)


def find_throw_combos(point_total, throw_score):
    """
    Recursive function to compute no. of combinations
    of throws that add up to make point_total.
    
    On the top layer we consider all multiples j of 4 st 4*j <= point_total,
    and pass the remainder r = point_total - 4 * j to the next level where
    we consider multiples of 3.
    
    NB: if the scores for different throws where not a sequence with step
    size == 1, we would store the values in a tuple and iterate through the
    tuple.
    """
    if throw_score == 2:
        # at bottom node of tree -> count leaves
        # ie no. of ways to sum to point_total with
        # 2- or 1-point throws
        return point_total // 2 + 1
    else:
        res = 0
        while point_total >= 0:
            res += find_throw_combos(point_total, throw_score - 1)
            point_total -= throw_score
        res %= MOD
        return res


if __name__ == '__main__':
    res = solution(1000)
    print(res)
