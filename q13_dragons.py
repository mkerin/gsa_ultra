# Please write your code inside the function stub below.
# python -m cProfile -s cumtime q13_dragons.py
import math
import itertools as it
from collections import namedtuple


class Point(object):
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta


class View(object):
    def __init__(self, pid, dist):
        self.pid = pid
        self.dist = dist


def solution(T):
    """
    We want to build an object that holds the
    for each angle theta holds
    - painting-id of closest painting
    - distance from origin of closest painting
    
    Question of how to choose what values of theta
    are contained in this object.
    Could scan all points, convert to values
    of theta, sort and then keep the midpoints.
    We can do this as no points are on same line
    through origin.
    This should mean we don't miss any paintings
    by having a 'resolution' thats too big.
    
    points: list of Named Tuples
    """
    
    # setup - mid_thetas, mid_vectors, V
    print("Generating points")
    points = []
    for x1, y1, x2, y2 in T:
        points.append(Point(x1, y1, XYtoTheta(x1, y1)))
        points.append(Point(x2, y2, XYtoTheta(x2, y2)))
    print("Points read in")
    points.sort(key=lambda x: x.theta)
    
    print("Generating midpoints")
    midpoints = GenMidpoints(points)
    V = [View(None, float("Inf")) for x in range(len(midpoints))]
    
    print("Evaluating closest paintings")
    for pid, p in enumerate(T):
        angle_to_edges = XYtoTheta(p[0], p[1]), XYtoTheta(p[2], p[3])
        r1, r2 = min(angle_to_edges), max(angle_to_edges)
        mid_index = [i for i, mid in enumerate(midpoints) if mid.theta > r1 and mid.theta < r2]
        for ind in mid_index:
            midpoint = midpoints[ind]
            d = DistFromOrigin(midpoint, p)
            if d < V[ind].dist:
                V[ind] = View(pid, d)

    visible = set(v.pid for v in V)
    res = len(visible)
    if None in visible:
        res -= 1
    return res


def XYtoTheta(x, y):
    """
    In range (0, 2pi] cos that's easier.
    """
    try:
        theta = math.atan2(y, x) + math.pi
    except TypeError:
        print(x, y)
        raise TypeError("a float is required")
    return theta


def DistFromOrigin(midpoint, painting):
    """
    Distance from origin using cramers rule
    https://en.wikipedia.org/wiki/Cramer%27s_rule
    """
    Lp = Line((painting[0], painting[1]), (painting[2], painting[3]))
    Lo = Line((midpoint.x, midpoint.y), (0, 0))
    x, y = Intersection(Lp, Lo)
    d = math.sqrt(x ** 2 + y ** 2)
    return d


def Line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C


def Intersection(L1, L2):
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = float(Dx) / D
        y = float(Dy) / D
        return x, y
    else:
        return False


def GenMidpoints(points):
    """
    :return:
    - midpoints: list of Points
        Point contains x, y coord and
        theta; angle from x, y to origin
    """
    # generate midpoints
    L = len(points)
    tmp1 = points[:L-1]
    tmp2 = points[1:L]
    midpoints = []
    for a, b in it.izip(tmp1, tmp2):
        mx, my = (a.x+b.x)/2, (a.y+b.y)/2
        midpoints.append(Point(mx, my, XYtoTheta(mx, my)))
    # special handling for midpoint across 0, 2pi
    a = points[0]
    b = points[L-1]
    mx, my = (a.x+b.x)/2, (a.y+b.y)/2
    bound = Point(mx, my, XYtoTheta(mx, my))
    if bound.theta < midpoints[0].theta and bound.theta > 0:
        midpoints.insert(0, bound)
    elif bound.theta > midpoints[L-2].theta and bound.theta <= 2 * math.pi:
        midpoints.append(bound)
    else:
        raise Exception("Boundary midpoint behaving unexpectedly")
    return midpoints


if __name__ == '__main__':
    with open("q13_input.txt") as f:
        T = []
        for line in f:
            p = [int(x) for x in line.rstrip("/n").split()]
            T.append(tuple(p))
    T = tuple(T)
    res = solution(T)
    print(res)
