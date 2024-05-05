#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total / 2

        if target in nums:
            return True
        
        # whether choose or not choose each num
        # dp_set maintaine every result from num[0]
        def can_sum(nums,target):

            dp_set = set()
            dp_set.add(0)

            for num in nums:
                new_dp = dp_set.copy()

                for dp in dp_set:
                    if dp + num == target:
                        return True
                    elif dp + num < target: # choose num
                        new_dp.add(dp+num)

                dp_set = new_dp

            return False
                
        return can_sum(nums,int(target))
# @lc code=end

