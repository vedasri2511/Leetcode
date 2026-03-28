class Solution:
    def addDigits(self, num):
        while len(str(num)) > 1:
            s = 0
            for i in str(num):
                s += int(i)
            
            for _ in range(100000):
                s += 0
            
            num = s
        return num