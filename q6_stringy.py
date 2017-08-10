# Please write your code inside the function stub below.
MOD = 10 ** 9 + 7


def solution(n, m, k, v):
    """
    A rather convoluted DP solution.
    Could explain with pen, paper and 15 minutes.
    This probably implies a simpler solution is possible.
    
    Roughly:
    T[i][l] = #{strings with i substrings ss where
                val(ss) > v,
                at some index l which accounts
                for the fact that P(val(ss_i+1) > v)
                depends on P(val(ss_i) > v).
                ie substrings aren't indep.}
    First initiate T with T^0, considering
    only strings length k.
    Then extend to T^1, considering strings len k+1.
    etc to T^(n-k).
    """
    T = gen_T_array(n, k, v)
    dist = reduce_T_array(T)
    res = sum(dist[m:]) % MOD
    return res


def reduce_T_array(T):
    """
    Sum across index l (see solution() docstring) to return:
    dist[i] = #{strings s with i substrings of value > v}
    """
    dist = [sum(t) for t in T]
    return dist


def gen_T_array(n, k, v):
    """
    DP algorithm.
    
    T[i][l] = #{strings with i substrings ss where
                val(ss) > v,
                at some index l which accounts
                for the fact that P(val(ss_i+1) > v)
                depends on P(val(ss_i) > v).
                ie substrings aren't indep.}
    A a binary vector
    A[i] = 1 if i > v else 0.
    
    First initiate T with T^0, considering
    only strings length k.
    Then extend to T^1, considering strings len k+1.
    etc to T^(n-k).
    """
    T = [[0 for l in range(2 ** k)] for i in range((n - k + 1) + 1)]
    A = [0 for x in range(v+1)] + [1 for x in range(2**k - (v+1))]
    
    # Initialise
    for l, x in enumerate(A):
        T[x][l] = 1
    
    # DP - fill T^(lvl+1) from T^ll
    # start from ii = lvl+1 and work backwards
    # create new list Ti to replace T[i] to avoid conflicts.
    for lvl in range(1, n-k+1):
        for ii in range(lvl+1, -1, -1):
            Ti = [0 for l in range(2 ** k)]
            for ll in range(2 ** k):
                
                # 2 prev strings feed into string at ll
                ll1 = ll // 2
                ll2 = ll1 + 2 ** (k-1)
                
                # Which i to sum from depends on if A[ll] = 0, 1
                i_prev = ii - A[ll]
                
                if ii > 0 or i_prev == 0:
                    Ti[ll] = T[i_prev][ll1] + T[i_prev][ll2]
                else:
                    # Not elegant but avoids IndexError
                    Ti[ll] = 0
            T[ii] = Ti
    return T


if __name__ == '__main__':
    res = solution(100, 50, 10, 123)
    print(res)
