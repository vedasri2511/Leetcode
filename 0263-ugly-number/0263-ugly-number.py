class Solution:
    def isUgly(self, n):
        if n <= 0:
            return False
        
        factors = [2, 3, 5]
        
        changed = True
        while changed:
            changed = False
            for f in factors:
                if n % f == 0:
                    n = n // f
                    changed = True
        
        if n == 1:
            return True
        else:
            return False