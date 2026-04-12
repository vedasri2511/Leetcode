class Solution:
    def intersection(self, a, b):
        return list({*a} & {*b})