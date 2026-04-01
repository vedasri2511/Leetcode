class Solution:
    def firstBadVersion(self, total_versions):
        left = 1
        right = total_versions
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return left