# Please write your code inside the function stub below.

# constants
MOD = (10 ** 9 + 7)
LIM = 1000

def solution(tuple_of_integers):
    """
    Back-tracking algo
    https://en.wikipedia.org/wiki/Backtracking
    """
    P = list(tuple_of_integers)
    count = solve(P, 0, len(P))
    return (count % MOD)


def solve(P, ind, N):
    """
    Recursive method to find unknowns that represent the size of the next file
    and fill in possible values.
    
    Params:
    - P:   the tuple_of_integers in list form.
    - ind: the current index being considered in P.
    - N:   length of the tuple_of_integers
    
    A file-size combination is valid if the end of the last file coincides
    with the end of the tuple_of_integers
    (ie ind_next = ind + P[ind] + 1; ind_next == N).
    
    Counting the number of possible files for a given file-size combination:
    - if valid increase count by 1000 * #{remaining -1's}
    - if invalid increase count by 0.
    """
    if ind > N:
        # Invalid file-size combo found.
        return 0
    elif ind == N:
        # Valid file-size combo found.
        res = num_of_ways(P)
        return res
    
    if P[ind] == -1:
        # Unknown found where we expect a file size.
        res = 0
        sol = 0
        while sol <= LIM and ind + sol <= N - 1:
            P[ind] = sol
            res += solve(P[:], ind, N)
            sol += 1
        return (res % MOD)
    else:
        # Go to next file-size indicator.
        ind += P[ind] + 1
        return solve(P, ind, N)


def num_of_ways(P):
    """
    For each remaining -1 there are LIM+1 ways to impute each file,
    where possible inputs are in range 0 - LIM.
    """
    return (LIM + 1) ** P.count(-1)


if __name__ == '__main__':
    with open('input/q8_input.txt', 'r') as f:
        tuple_of_integers = tuple([int(x.strip('\r\n')) for x in f.readlines()])
    print("Running on test case: {}".format(tuple_of_integers))
    res = solution(tuple_of_integers)
    print(res)
