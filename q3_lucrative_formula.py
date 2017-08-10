# Please write your code inside the function stub below.
import math


def solution(test_cases):
    """
    Each test case that Emma runs can be viewed as a k-ary tree,
    where k = 2 ** B and B is the number of bottles used.
    Hence the question becomes; what is the minimum B such that Emma's
    'test tree' with depth D = {num_of_days} has >= N leaves.
    """
    res = []
    for N, D in test_cases:
        B = min_bottles(N, D)
        res.append(str(B))
    return "".join(res)


def min_bottles(n, d):
    """Minimum integer b st 2 ** (b*d) >= n."""
    res = math.ceil(1.0/d * math.log(n, 2))
    return int(res)


if __name__ == '__main__':
    test_cases = []
    with open('input/q3_input.txt', 'r') as f:
        for line in f:
            test_cases.append(tuple(int(x) for x in line.strip('\r\n').split()))
    test_cases = tuple(test_cases)
    print("Running on test case: {}".format(test_cases))
    res = solution(test_cases)
    print(res)
