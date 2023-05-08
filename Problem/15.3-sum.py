#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[j] + nums[k] + nums[i] == 0:
                    if [nums[i],nums[j],nums[k]] not in ans:
                        ans.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                if nums[j] + nums[k] + nums[i] > 0:
                    k -= 1
                elif nums[j] + nums[k] + nums[i] < 0:
                    j += 1

        return ans
# @lc code=end

