class Solution:
    def isValidSudoku(self, b):
        s = set()
        return not any(
            (c!='.' and ((i,c) in s or (c,j) in s or (i//3,j//3,c) in s or s.add((i,c)) or s.add((c,j)) or s.add((i//3,j//3,c))))
            for i in range(9) for j,c in enumerate(b[i])
        )