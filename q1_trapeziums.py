# Please write your code inside the function stub below.
# python -m cProfile -s cumtime q1_trapeziums.py

import itertools as it
from fractions import gcd
import math


def GenOrthDistFromOrigin(p1, v1):
    """
    Orthogonal distance from the origin to the vector
    defined by p1 + v1.
    Return as +ve if in y >= 0 plane.
    """
    if p1 == (0, 0):
        return 0
    orth_vec = -1 * v1[1], v1[0]
    L1 = Line(p1, (p1[0] + v1[0], p1[1] + v1[1]))
    L2 = Line((0, 0), orth_vec)
    try:
        x, y = Intersection(L1, L2)
    except TypeError:
        print(p1, v1, orth_vec)
        raise TypeError
    d = Dist((0, 0), (x, y))
    if y >= 0:
        return d
    else:
        return -d


def GenParrallelPts(D):
    pass


def solution(D):
    """
    Save vectors from each point to a dict
    Should give all parrallel lines.
    """
    # Create dict of parrallel lines
    print("Create Parrallel points")
    parrallel_pts = dict()
    vectors_dict = dict()
    for pair in it.combinations(D, 2):
        unit_vec = GenVector(pair[0], pair[1])
        orth_dist = GenOrthDistFromOrigin(pair[0], unit_vec)
        vectors_dict[pair] = unit_vec
        
        if unit_vec not in parrallel_pts:
            parrallel_pts[unit_vec] = dict()
        parrallel_pts[unit_vec].setdefault(orth_dist, []).append(pair)

    # Want vectors parrallel to multiple pairs
    parrallel_pts = {key: val for key, val in parrallel_pts.items() if len(val) > 1}
    
    # Compute areas.
    A = 0
    for unit_vec, inner_dict in parrallel_pts.items():
        for orth_dist1, orth_dist2 in it.combinations(inner_dict.keys(), 2):
            for pair1, pair2 in it.product(inner_dict[orth_dist1],
                                           inner_dict[orth_dist2]):
                x = Dist(pair1[0], pair1[1])
                y = Dist(pair2[0], pair2[1])
                h = abs(orth_dist2 - orth_dist1)
                a = (x+y) * h / 2
                if IsRhombus1(pair1, pair2, vectors_dict):
                # if IsRhombus3(pair1, pair2, unit_vec):
                    a *= 0.5
                A += a
    return "{:0.2f}".format(10*A).replace(".", "")


def GenVector(p1, p2, irred=True):
    """
    Return vector from one point to the other.
    Preferably with same orientation + irreducible.
    """
    res = [p1[0] - p2[0], p1[1] - p2[1]]
    if irred:
        k = gcd(res[0], res[1])
        if k == 0:
            k = 1
        res = (res[0] // k, res[1] // k)
    return tuple(res)


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
        print(L1, L2)
        return False


def Dist(p1, p2):
    """Distance between two points (x1, y1), (x2, y2)."""
    d = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    return d


def DictLookup(point1, point2, vectors_dict):
    """
    Order of keys matters
    """
    if (point1, point2) in vectors_dict:
        vec = vectors_dict[(point1, point2)]
    else:
        vec = vectors_dict[(point2, point1)]
    return vec


def IsRhombus3(pair1, pair2, unit_vec):
    # Check to for other parralel lines
    tol = 0.00001
    p1, _ = pair1
    orth_vec = -1 * unit_vec[1], unit_vec[0]
    for p in pair2:
        if 0 in orth_vec:
            j = orth_vec.index(0)
            if p1[j] != p[j]:
                break
            else:
                return True
        tx = float(p1[0] - p[0]) / orth_vec[0]
        ty = float(p1[1] - p[1]) / orth_vec[1]
        if abs(tx - ty) < tol:
            return True
    return False


def IsRhombus1(pair1, pair2, vectors_dict):
    # Check to for other parralel lines
    l1 = DictLookup(pair1[0], pair2[0], vectors_dict)
    l2 = DictLookup(pair1[1], pair2[1], vectors_dict)
    l3 = DictLookup(pair1[0], pair2[1], vectors_dict)
    l4 = DictLookup(pair1[1], pair2[0], vectors_dict)
    if len(set([l1, l2, l3, l4])) < 4:
        return True
    return False


def IsRhombus2(pair1, pair2):
    # Check for other parralel lines
    l1 = GenVector(pair1[0], pair2[0], irred=False)
    l2 = GenVector(pair1[1], pair2[1], irred=False)
    l3 = GenVector(pair1[0], pair2[1], irred=False)
    l4 = GenVector(pair1[1], pair2[0], irred=False)
    if IsParrallel(l1, l2) or IsParrallel(l3, l4):
        return True
    return False


def IsParrallel(v1, v2):
    epsilon = 0.000001
    scalar_product = sum(i[0] * i[1] for i in zip(v1, v2))
    length1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
    length2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
    if scalar_product/(length1*length2) > 1 - epsilon:
        return True
    return False


if __name__ == '__main__':
    D = []
    with open('q1_input.txt') as f:
        for line in f:
            c1, c2 = line.rstrip("/n").split()
            D.append((int(c1), int(c2)))
    D = tuple(D)
    res = solution(D)
    print(res)
