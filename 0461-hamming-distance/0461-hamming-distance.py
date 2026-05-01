class Solution:
    def hammingDistance(self, x, y):
        n = x ^ y
        cnt = 0
        
        while n:
            n &= n - 1
            cnt += 1
            
        return cnt