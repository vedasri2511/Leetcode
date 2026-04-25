class Solution:
    def thirdMax(self, nums):
        a = b = c = float('-inf')

        for x in nums:
            if x in (a, b, c):
                continue
            if x > a:
                a, b, c = x, a, b
            elif x > b:
                b, c = x, b
            elif x > c:
                c = x

        return c if c != float('-inf') else a