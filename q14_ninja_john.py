# Please write your code inside the function stub below.
import copy


def solution(tuple_of_test_cases):
    costs = []
    for n, j, D in tuple_of_test_cases:
        if sum(D) > (n + 1) * j:
            print("Not possible - pass")
        else:
            excess, edges = preprocess(j, D)
            cost = solve(excess, edges)
            costs.append(str(cost))
    return "".join(costs)


def solve(excess, edges):
    """
    Recursively merge adjacent elements of excess,
    where edges[i] holds the cost of merging excess[i] + excess[i+1].
    This is similar to a depth first search of a tree.
    Return minimum cost.
    """
    if all(ex <= 0 for ex in excess):
        return 0
    else:
        res = float("Inf")
        for i in range(len(edges)):
            new_excess = copy.copy(excess)
            new_edges = copy.copy(edges)
            new_excess[i:i+2] = [new_excess[i] + new_excess[i+1]]
            cost = new_edges.pop(i)
            v = solve(new_excess, new_edges)
            res = min(res, v + cost)
        return res


def preprocess(j, D):
    """
    Compute distance between elements d of D where d != j.
    If d = j, then 'merge' with adjacent element end increase
    edge cost.
    """
    D_prime = [d - j for d in D]
    excess = []
    edges = []
    cost = 1
    for d in D_prime:
        if d == 0:
            cost += 1
        else:
            excess.append(d)
            edges.append(cost)
            cost = 1
    edges.pop(0)  # 'Ninja John' starts here.
    return excess, edges


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
