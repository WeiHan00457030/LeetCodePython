#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        dp_lists = []
        dp_lists.append([])

        for num in nums:
            new_dp_lists = dp_lists.copy()
            for subset in dp_lists:
                new_subset = subset.copy()
                new_subset.append(num)
                new_dp_lists.append(new_subset)
            
            dp_lists = new_dp_lists
        
        
        return dp_lists
    
# @lc code=end

