#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows ,cols = len(matrix),len(matrix[0])
        result = []
        i,j=0,0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        directionIndex = 0
       
        result.append(matrix[0][0])
        matrix[0][0] = -999
            
        while len(result) < rows * cols:
            direction = directions[directionIndex % 4]

            nextI = i + direction[0]
            nextJ = j + direction[1]

            if 0 <= nextI < rows and 0 <= nextJ < cols and matrix[nextI][nextJ] >= -100:
                result.append(matrix[nextI][nextJ])
                matrix[nextI][nextJ] = -999
                i,j = nextI,nextJ
            else:
                directionIndex += 1

           
        return result



        
            
# @lc code=end

