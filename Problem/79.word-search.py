#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def find(i,j,word_index):
            
            if word_index == 1:
                walked = []

            for direction in directions:

                next_i = i + direction[0]
                next_j = j + direction[1]

                if 0 <= next_i < len(board) and 0 <= next_j < len(board[0]) and [next_i,next_j] not in walked and board[next_i][next_j] == word[word_index]:
                    walked.append([next_i,next_j])
                    if word_index == len(word)-1:
                        return True
                    
                    return find(next_i,next_j,word_index+1)
        
        walked = []

        for i in range(len(board)):
            for j in range(len(board[0])):

                letter = board[i][j]
                if letter == word[0]:
                    if find(i,j,1):
                        return True

        return False
            
# @lc code=end

