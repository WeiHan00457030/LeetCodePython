#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        count = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def visitIslands(x,y):
            grid[x][y] = '2'
            for i,j in directions:
                if 0<= i+x < len(grid) and 0 <= j+y < len(grid[0]) and grid[i+x][j+y] == '1':
                    visitIslands(i+x,j+y)


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    visitIslands(x,y)
                    count += 1
        return count
    
    
# @lc code=end

