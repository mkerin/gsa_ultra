# Please write your code inside the function stub below.


def solution(cost, starting_tokens):
    p = 7
    x0s = [1.0 / y for y in range(-1, 1, 1.0 / 2*p)]
    print(x0s)
    for x0 in x0s:
        root = Newton(f, df, x0, 1e-5)
    pass


def Newton(f, df, x0, e):
    """
    Implementation of Newton-Raphson
    """
    delta = dx(f, x0)
    while delta > e:
        x0 = x0 - f(x0)/df(x0)
        delta = dx(f, x0)
    print 'Root is at: ', x0
    print 'f(x) at root is: ', f(x0)


def dx(f, x):
    return abs(0-f(x))


def f(x):
    p = 7
    return x ** (p+2) - 2 * x ** (p) - 1


def df(x):
    p = 7
    return (p + 2) * x ** (p + 1) - 2 * p * x ** (p - 1)


if __name__ == '__main__':
    res = solution(7, 1000)
    print(res)
