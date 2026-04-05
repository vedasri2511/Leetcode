class NumArray(object):

    def __init__(self, nums):
        self.pref = [0] * (len(nums) + 1)
        
        for idx in range(len(nums)):
            self.pref[idx + 1] = self.pref[idx] + nums[idx]

    def sumRange(self, left, right):
        return self.pref[right + 1] - self.pref[left]