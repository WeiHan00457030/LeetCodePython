#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions =[[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(idx):
            
            cur = heights[idx[0]][idx[1]]
            
            for direction in directions:
                
                nxt_row = idx[0] + direction[0]
                nxt_col = idx[1] + direction[1]
                
                if 0 <= nxt_row < len(heights) and 0 <= nxt_col < len(heights[0]):

                    nxt = heights[nxt_row][nxt_col]
                    #print(f"cur:{cur}, nxt:{nxt}")

                    if cur <= nxt  and (nxt_row, nxt_col) not in dfs_set:
                        dfs_set.add((nxt_row, nxt_col))
                        
                        dfs([nxt_row,nxt_col])

        dfs_set = set()
        pacific = set()
        # dfs from pacific ocean
        for i in range(len(heights)):
            if (i, 0) not in dfs_set:
                dfs_set.add((i, 0))
                dfs((i, 0))
        for i in range(len(heights[0])):
            if (0, i) not in dfs_set:
                dfs_set.add((0, i))
                dfs((0, i))

        # store and reset
        pacific = dfs_set
        dfs_set = set()

        # dfs from Atlantic ocean
        for i in range(len(heights)):
            if (i, len(heights[0])-1) not in dfs_set:
                dfs_set.add((i, len(heights[0])-1))
                dfs((i, len(heights[0])-1))

        for i in range(len(heights[0])):
            if (len(heights)-1, i) not in dfs_set:
                dfs_set.add((len(heights)-1, i))
                dfs((len(heights)-1, i))
        
        ans = []
        for st in dfs_set:
            if st in pacific:
                ans.append([st[0],st[1]])
        
        return ans

# @lc code=end

