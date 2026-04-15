# The guess API is already defined for you.
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n):
        l, r = 1, n

        while l <= r:
            m = l + (r - l) // 2
            g = guess(m)

            if g == 0:
                return m
            elif g < 0:
                r = m - 1
            else:
                l = m + 1