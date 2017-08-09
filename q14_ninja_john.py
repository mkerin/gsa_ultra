# Please write your code inside the function stub below.


def solution(tuple_of_test_cases):
    """
    This seems like a 2D DP problem
    """
    for n, j, D in tuple_of_test_cases:
        print(tuple([n, j, D]))
        # possible?
        if sum(D) > (n + 1) * j:
            print("Not possible - pass")
    pass


if __name__ == '__main__':
    with open('q14_input.txt') as f:
        lines = f.read().split("\r\n")
    test_cases = []
    print(lines)
    for mm in range(len(lines) // 2):
        n, m = [int(x) for x in lines[2*mm].split()]
        hey = [int(x) for x in lines[2*mm + 1].split()]
        # print("{} -> {}".format(2*mm, [n, m]))
        # print("{} -> {}".format(2*mm+1, hey))
        test_cases.append(tuple([n, m, tuple(hey)]))
    test_cases = tuple(test_cases)
    res = solution(test_cases)
    print(res)
