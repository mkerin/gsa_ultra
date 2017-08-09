# Please write your code inside the function stub below.
# python -m cProfile -s cumtime q1_trapeziums.py

import itertools as it
from fractions import gcd
import math


def solution(D):
    """
    General approach:
    1. Examine all possible line-segments and compute a 'unit' vector and
       the orthogonal distance between this unit vector and the origin.
    2. Store line-segments in a dict of dicts: parallel_pts.
       The upper dict holds dicts of all parallel line-segments, and the
       lower dict stores the length of line segments occurring on the same
       plane.
    3. Filter segments that are only parallel to others on the same plane.
       ie the Area is zero.
    4. Compute the sum of all trapezium areas, noting that if two parallel
       line segments are the same length this implies a rhombus has occurred.
    """
    print("Create nested dicts of parallel points on the same plane")
    parallel_pts = dict()
    for pair in it.combinations(D, 2):
        unit_vec = GenVector(pair[0], pair[1])
        orth_dist = GenOrthDistFromOrigin(pair[0], unit_vec)
        
        if unit_vec not in parallel_pts:
            parallel_pts[unit_vec] = dict()
        x = Dist(pair[0], pair[1])
        parallel_pts[unit_vec].setdefault(orth_dist, []).append(x)

    # Want vectors parrallel to multiple pairs
    parallel_pts = {key: val for key, val in parallel_pts.items() if len(val) > 1}
    
    # Compute area of all trapeziums with formula (x + y) * h / 2
    # if opposite side lengths are identical -> we have a trapezium, hence
    # compute only half area a = x * h / 2
    A = 0
    for unit_vec, inner_dict in parallel_pts.items():
        for orth_dist1, orth_dist2 in it.combinations(inner_dict.keys(), 2):
            h = abs(orth_dist2 - orth_dist1)
            segs = sum(x if x == y else x+y for x, y in it.product(inner_dict[orth_dist1], inner_dict[orth_dist2]))
            A += segs * h / 2

    return "{:0.2f}".format(10*A).replace(".", "")


def GenOrthDistFromOrigin(p1, v1):
    """
    Orthogonal distance from the origin to the vector p1 + t * v1.
    Return as +ve if in y >= 0 plane.
    """
    if p1 == (0, 0):
        return 0
    orth_vec = -1 * v1[1], v1[0]
    L1 = LineTriple(p1, (p1[0] + v1[0], p1[1] + v1[1]))
    L2 = LineTriple((0, 0), orth_vec)
    x, y = Intersection(L1, L2)
    d = Dist((0, 0), (x, y))
    if y >= 0:
        return d
    else:
        return -d


def GenVector(p1, p2):
    """
    Return a 'unit' vector from one p1 = (x1, y1) to p2 = (x2, y2),
    with irreducible, integer components.
    """
    unit_vec = [p1[0] - p2[0], p1[1] - p2[1]]
    k = gcd(unit_vec[0], unit_vec[1])
    if k == 0:
        k = 1
    unit_vec = (unit_vec[0] // k, unit_vec[1] // k)
    return tuple(unit_vec)


def Intersection(L1, L2):
    """
    Intersection of two lines computed with Cramers Rule:
    https://en.wikipedia.org/wiki/Cramer%27s_rule
    """
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = float(Dx) / D
        y = float(Dy) / D
        return x, y
    else:
        print(L1, L2)
        return False


def LineTriple(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C


def Dist(p1, p2):
    """Distance between two points (x1, y1), (x2, y2)."""
    d = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    return d


if __name__ == '__main__':
    D = []
    N = 20
    with open('q1_input.txt') as f:
        for n, line in enumerate(f):
            c1, c2 = line.rstrip("/n").split()
            D.append((int(c1), int(c2)))
            if n > N:
                break
    D = tuple(D)
    res = solution(D)
    print(res)
