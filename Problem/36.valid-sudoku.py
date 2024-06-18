#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                
                if board[i][j] == ".":
                    continue
                
                squares_index = 3*(i//3) + j//3
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[squares_index]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[squares_index].add(board[i][j])

        return True
# @lc code=end

