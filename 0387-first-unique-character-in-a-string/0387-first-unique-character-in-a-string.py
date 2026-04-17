class Solution:
    def firstUniqChar(self, s):
        return min([s.index(c) for c in set(s) if s.count(c) == 1] or [-1])