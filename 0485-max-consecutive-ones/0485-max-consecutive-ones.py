class Solution:
    def findMaxConsecutiveOnes(self, nums):
        cur = ans = 0

        for x in nums:
            if x:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0

        return ans