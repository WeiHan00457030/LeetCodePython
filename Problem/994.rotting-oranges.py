#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rottening = True
        rottenList = []
        minutes = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottenList.append([i,j])

        while(rottening):
            rottening = False
            newRotten = []
            for rotten in rottenList:
                i,j = rotten
                for direction in directions:
                    if len(grid) > i+direction[0] >= 0 and len(grid[0]) > j+direction[1] >= 0: 

                        if grid[i+direction[0]][j+direction[1]] == 1:
                            if not rottening:
                                rottening = True
                            newRotten.append([i+direction[0],j+direction[1]])
                            grid[i+direction[0]][j+direction[1]] = 2
            if rottening:
                minutes += 1          
            rottenList = newRotten

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1  
                             
        return minutes
# @lc code=end

