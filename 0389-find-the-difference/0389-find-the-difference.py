from functools import reduce

class Solution:
    def findTheDifference(self, s, t):
        return chr(reduce(lambda x, y: x ^ y, map(ord, s + t)))