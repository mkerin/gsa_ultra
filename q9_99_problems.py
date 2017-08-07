# Please write your code inside the function stub below.

LIM = 1000

def solution(tuple_of_integers):
    """
    Back-tracking algo
    https://en.wikipedia.org/wiki/Backtracking
    """
    P = list(tuple_of_integers)
    print("tuple of length = {}".format(len(P)))
    count = solve(P, 0, len(P))
    return count


def solve(P, ind, N):
    """
    Traverse a LIM-ary tree.

    At each node I test a new value for the size |L|
    of the next file, where previously it was unknown.

    Leaf node occurs when all file sizes are filled in.
    - if viable increase count by 1000 * #{remaining -1's}
    - if not viable increase count by 0.
    """

    print("New Recursion, IND = {}, P = {}".format(ind, P))
    if ind > N - 1:
        print("Index overflow")
        return 0

    if P[ind] == -1:
        print("imputing, ind = {}". format(ind))
        # impute
        res = 0
        sol = 0
        while sol <= LIM and ind + sol <= N - 1:
            P[ind] = sol
            print("P = {},i = {}".format(P, ind))
            res += solve(P[:], ind, N)
            sol += 1
        print("Finished imputing")
        return res
    else:
        print("transition")
        # at end of list & list not viable
        if ind + P[ind] > N - 1:
            print("Non-viable solution found")
            return 0

        # at end of list & list viable
        if ind + P[ind] == N - 1:
            print("Viable solution found")
            res = num_of_ways(P)
            return res

        # not at end of list
        ind += P[ind] + 1
        return solve(P, ind, N)
#
# P = [-1, 2, 3, -1, 4, 5, -1, 6, 7, -1]
# solve(P, 0, len(P))

def num_of_ways(P):
    """
    For each remaining -1 there are 1001 possible ways to
    impute file.
    """
    print("Leaf node! P = {}".format(P))
    print("count = {}".format((LIM + 1) * P.count(-1)))
    return (LIM + 1) * P.count(-1)
