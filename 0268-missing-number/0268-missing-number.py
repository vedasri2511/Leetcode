class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        
        total_xor = 0
        arr_xor = 0
        
        for i in range(n + 1):
            total_xor ^= i
        
        for num in nums:
            arr_xor ^= num
        
        return total_xor ^ arr_xor