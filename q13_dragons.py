# Please write your code inside the function stub below.
# python -m cProfile -s cumtime q13_dragons.py
import math
import itertools as it


def solution(T):
    """
    Compute the painting-id (pid) of the closest painting to the origin
    at a set number of values theta.

    To choose pertinent values of theta:
    1. Scan all points regardless of pid
    2. Sort by values of theta
    3. Compute midpoints; list of class objects Midpoint
    NB: Possible as no 2 points on same line through origin.
    
    Then for each Midpoint, store the pids of paintings that could be
    seen from that rotation.

    Finally compute the closest painting in each case.
    """
    print("Scanning / sorting points")
    points = []
    for pid, (x1, y1, x2, y2) in enumerate(T):
        r1, r2 = XYtoTheta(x1, y1), XYtoTheta(x2, y2)
        s1, s2 = CalcSides(r1, r2)
        points.append(Point(x1, y1, r1, pid, s1))
        points.append(Point(x2, y2, r2, pid, s2))
    print("Points read in")
    points.sort(key=lambda x: x.theta)
    
    print("Generating midpoints")
    midpoints = GenMidpoints(points)
    V = [View(None, float("Inf")) for x in range(len(midpoints))]
    
    print("Computing pids that intersect with each midpoint")
    all_points = midpoints + points
    all_points.sort(key=lambda x: x.theta)
    active_pids = set()
    second_loop_j = None
    for j, aa in enumerate(all_points):
        # print(aa)
        if aa.pid is None:
            # a midpoint
            aa.pids_inline.update(active_pids)
        else:
            # point defining the edge of a painting
            if aa.side == "r":
                active_pids.add(aa.pid)
            else:
                try:
                    active_pids.remove(aa.pid)
                except KeyError:
                    # implies painting crosses 0 / 2pi boundary
                    second_loop_j = j
    # Second loop neessary for paintings that cross 0, 2pi boundary
    if second_loop_j is not None:
        for j, aa in enumerate(all_points[:second_loop_j]):
            if aa.pid:
                # a midpoint
                aa.pids_inline.update(active_pids)
            else:
                # point defining the edge of a painting
                if aa.side == "r":
                    active_pids.add(aa.pid)
                else:
                    try:
                        active_pids.remove(aa.pid)
                    except KeyError:
                        raise KeyError("Shouldn't happen on second loop")
    
    print("Evaluating closest paintings")
    midpoints = [m for m in all_points if m.pid is None]
    for ind, midpoint in enumerate(midpoints):
        # print(midpoint)
        for pid in midpoint.pids_inline:
            p = T[pid]
            d = DistFromOrigin(midpoint, p)
            if d < V[ind].dist:
                V[ind] = View(pid, d)

    visible = set(v.pid for v in V)
    res = len(visible)
    if None in visible:
        res -= 1
    return res


def CalcSides(r1, r2):
    """
    As you looking at painting in field of view (r1, r2), is r1 on the right
    or the left?
    
    Params:
    r1 - angle from origin to (x1, y1) in radians
    r2 - angle from origin to (x2, y2) in radians
    """
    if abs(r1 - r2) > math.pi:
        # lies across the theta = 0, theta = 2pi boundary
        if r1 < r2:
            s1 = "l"
            s2 = "r"
        else:
            s1 = "r"
            s2 = "l"
    else:
        # normal - no special treatment
        if r1 > r2:
            s1 = "l"
            s2 = "r"
        else:
            s1 = "r"
            s2 = "l"
    return s1, s2


def XYtoTheta(x, y):
    """In range (0, 2pi] cos that's easier."""
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
    """For use in DistFromOrigin."""
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C


def Intersection(L1, L2):
    """For use in DistFromOrigin."""
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
    Return a list of object of class Midpoint.

    Params:
    points - list of objects of class Point
    """
    # generate midpoints
    L = len(points)
    tmp1 = points[:L-1]
    tmp2 = points[1:L]
    midpoints = []
    for a, b in it.izip(tmp1, tmp2):
        mx, my = (a.x+b.x)/2, (a.y+b.y)/2
        midpoints.append(Midpoint(mx, my, XYtoTheta(mx, my)))
    # special handling for midpoint across 0, 2pi
    a = points[0]
    b = points[L-1]
    mx, my = (a.x+b.x)/2, (a.y+b.y)/2
    bound = Midpoint(mx, my, XYtoTheta(mx, my))
    if bound.theta < midpoints[0].theta and bound.theta > 0:
        midpoints.insert(0, bound)
    elif bound.theta > midpoints[L-2].theta and bound.theta <= 2 * math.pi:
        midpoints.append(bound)
    else:
        raise Exception("Boundary midpoint behaving unexpectedly")
    return midpoints


class Point(object):
    def __init__(self, x, y, theta, pid, side):
        self.x = x
        self.y = y
        self.theta = theta
        self.pid = pid
        # Look at the painting, is this point on the left or right?
        self.side = side

    def __str__(self):
        res = ["Point", self.theta, self.pid, self.side]
        res = [str(x) for x in res]
        return ", ".join(res)


class Midpoint(object):
    """
    Midpoint would inherit from point but
    super(Midpoint, self)._init_() is disabled.
    """
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
        self.pid = None
        self.side = None
        self.pids_inline = set()

    def __str__(self):
        res = ["Midpoint", self.theta, self.pids_inline]
        res = [str(x) for x in res]
        return ", ".join(res)


class View(object):
    def __init__(self, pid, dist):
        self.pid = pid
        self.dist = dist


if __name__ == '__main__':
    with open("q13_input.txt") as f:
        T = []
        for line in f:
            p = [int(x) for x in line.rstrip("/n").split()]
            T.append(tuple(p))
    T = tuple(T)
    res = solution(T)
    print(res)
