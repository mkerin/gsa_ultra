# Please write your code inside the function stub below.

import itertools as it
from fractions import gcd
import math


def solution(D):
    """
    Save vectors from each point to a dict
    Should give all parrallel lines.
    """
    # Create dict of parrallel lines
    vecs = dict()
    for pair in it.combinations(D, 2):
        vec = GenVector(pair[0], pair[1])
        if vec not in vecs:
            vecs[vec] = []
        vecs[vec].append(pair)
    
    # Compute areas.
    A = 0
    for key, val in vecs.items():
        if len(val) >= 2:
            for pts1, pts2 in it.combinations(val, 2):
                a = Area(pts1, pts2)
                if IsRhombus2(pts1, pts2):
                    a *= 0.5
                A += a
    return A


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


def Area(pair1, pair2):
    """
    Compute area from pairs,
    assumed that they define parrallel lines.
    pair1: a tuple
        eg. pair1 = ((x1, y1), (x2, y2))
    Similar for pair2.
    A = (a+b) * h / 2
    """
    a = Dist(pair1[0], pair1[1])
    b = Dist(pair2[0], pair2[1])
    # compute h; http://preview.tinyurl.com/ybgymuon
    w = (pair1[0][0] - pair2[0][0], pair1[0][1] - pair2[0][1])
    v = pair1[0][0] - pair1[1][0], pair1[0][1] - pair1[1][1]
    mag = float(sum(i[0] * i[1] for i in zip(w, v))) / sum([v[0] ** 2 + v[1] ** 2])
    v_orth = w[0] - mag * v[0], w[1] - mag * v[1]
    h = math.sqrt(v_orth[0] ** 2 + v_orth[1] ** 2)
    
    return (a+b) * h / 2


def Dist(p1, p2):
    # Distance between two points
    d = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    return d


def IsRhombus1(pts1, pts2):
    # Check to for other parralel lines
    l1 = GenVector(pts1[0], pts2[0])
    l2 = GenVector(pts1[1], pts2[1])
    l3 = GenVector(pts1[0], pts2[1])
    l4 = GenVector(pts1[1], pts2[0])
    if len(set([l1, l2, l3, l4])) < 4:
        return True
    return False


def IsRhombus2(pts1, pts2):
    # Check for other parralel lines
    l1 = GenVector(pts1[0], pts2[0], irred=False)
    l2 = GenVector(pts1[1], pts2[1], irred=False)
    l3 = GenVector(pts1[0], pts2[1], irred=False)
    l4 = GenVector(pts1[1], pts2[0], irred=False)
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
    # print(res)
