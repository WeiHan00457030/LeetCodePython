#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur,left = 0,0
        right = len(nums)-1

        while cur <= right:
            #print(nums,cur,left,right)
            if nums[cur] == 0:
                tmp = nums[cur]
                nums[cur] = nums[left]
                nums[left] = tmp
                left += 1
                cur += 1
            elif nums[cur] == 2:
                tmp = nums[cur]
                nums[cur] = nums[right]
                nums[right] = tmp
                right -= 1
            else:
                cur += 1
        
# @lc code=end

