class Solution:
    def islandPerimeter(self, grid):
        land = shared = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    land += 1
                    
                    if i > 0 and grid[i-1][j]:
                        shared += 1
                    if j > 0 and grid[i][j-1]:
                        shared += 1

        return land * 4 - shared * 2