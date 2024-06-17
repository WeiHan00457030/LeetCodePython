#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 從後往前找第一個降序
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        #數字已是最大
        if i == -1:
            nums[:] = sorted(nums)

        #從後往前找第一個比nums[i]大的
        j = len(nums)-1
        while j>=0 and nums[j] <= nums[i]:
            j -= 1
        
        #交換
        nums[i],nums[j] = nums[j],nums[i]

        #排序i後面的數
        nums[i+1:len(nums)]=sorted(nums[i+1:])
        

# @lc code=end

