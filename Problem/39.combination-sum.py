#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(cur_sum,combination,idx):
            # return while meet target
            if cur_sum == target:
                ans.append(combination)
                return
            # dfs all possible combination but index can't go backward
            for i in range(idx,len(candidates)):
                if cur_sum + candidates[i] <= target:
                    dfs(cur_sum + candidates[i], combination + [candidates[i]],i)                    
                    
        dfs(0,[],0)
        return ans             
# @lc code=end
   
