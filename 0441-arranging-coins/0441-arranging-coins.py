class Solution:
    def arrangeCoins(self, n):
        l, r = 0, n
        while l <= r:
            m = (l + r) // 2
            if m * (m + 1) // 2 <= n:
                l = m + 1
            else:
                r = m - 1
        return r