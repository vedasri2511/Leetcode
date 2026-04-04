class Solution(object):
    def canWinNim(self, stones):
        if stones % 4 == 0:
            return False
        return True