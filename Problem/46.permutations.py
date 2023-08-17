#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        
        def dfs (numList,permutation):
            if not numList :
                permutations.append(permutation)
            for num in numList:
                dfs(numList[:numList.index(num)] + numList[numList.index(num)+1:],permutation+[num])

        dfs(nums,[])
        return permutations
# @lc code=end

