#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmpList = {}
        for m in range(len(nums)):
            minusTarget = target - nums[m]

            if minusTarget in tmpList:
                return [tmpList[minusTarget],m]
            else:
                tmpList[nums[m]] = m
# @lc code=end
