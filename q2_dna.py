# Please write your code inside the function stub below.

from collections import Counter


def solution(s, x, y):
    """
    Consider the string as a
    - beginning segment from x:len(s) where s is the base string
    - middle segment of k * s
    - end segment :y of s.
    Then use a Counter to compute the dominant sequence.
    """
    n = len(s)
    if y <= n:
        # Case 1: x, y both fall in first repeat of base sequence s
        counter = Counter(s[x:y+1])
    else:
        # Case 2: y in a different repeat of base sequence s
        if x > n:
            # Case 2.5: x starts in next repeat of base sequence s.
            # Adjust x, y accordingly.
            y -= x - (x % n)
            x %= n
        # k = Number of repeats of base sequence
        k = (y // n) - 1
        r = y % n
        # forming component parts of the counter
        beg = Counter(s[x:]) 
        mid = Counter(s)
        for key in mid.keys():
            mid[key] *= k
        end = Counter(s[:r+1])
        counter = beg + mid + end
    
    most_common = counter.most_common()
    if most_common[0][1] == most_common[1][1]:
        return 0
    else:
        return most_common[0][1]
