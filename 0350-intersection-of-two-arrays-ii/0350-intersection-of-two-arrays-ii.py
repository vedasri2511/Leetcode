from collections import Counter

class Solution:
    def intersect(self, a, b):
        c = Counter(a)
        return [x for x in b if c[x] > 0 and not c.__setitem__(x, c[x]-1)]