#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count = 1
        for i in nums:
            if i not in nums[0:count]:
                nums[count] = i
                count +=1
        
        return count

# @lc code=end

