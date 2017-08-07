# Please write your code inside the function stub below.


def solution(n):
    """
    Winning strategy:
    1. return a triangle where the
       number of counters on each
       vertex are the same.
    2. You win.
    There are n+1 games where this
    isn't possible for Alice as the
    game starts in an equal state.
    """
    return (n+1) ** 3 - (n+1)
