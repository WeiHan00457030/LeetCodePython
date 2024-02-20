#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()

        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                tmp = nums[i] + nums[j ] + nums[k]
                if tmp == 0:
                    ans.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif tmp>0:
                    k-=1
                else:
                    j+=1
        return ans
# @lc code=end

