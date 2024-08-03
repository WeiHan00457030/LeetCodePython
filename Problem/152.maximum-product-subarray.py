#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from math import inf
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ans = -inf
        
        # split list with 0
        split_lists = []
        last_index = -1
        for idx,num in enumerate(nums):
            if num == 0:
                ans = 0
                if idx > 0:
                    split_lists.append(nums[last_index+1:idx])
                last_index = idx

        if last_index < len(nums)-1:
            split_lists.append(nums[last_index+1:])
        
        for sublist in split_lists:

            tmp = 1
            first_neg_index = -1

            # product always get larger abs value, we only care about the symbol +/-
            for idx,num in enumerate(sublist):
                tmp *= num
                if tmp > ans:
                    ans = tmp
                if num < 0 and first_neg_index == -1:
                    first_neg_index = idx


            # if tmp is negative, means there have odd neg numbers
            # divide until the first neg num
            if tmp < 0 and abs(tmp) > ans and len(sublist) > 1:
                for num in sublist[:first_neg_index+1]:
                    tmp /= num
                    if tmp > ans:
                        ans = tmp

        return int(ans)

# @lc code=end

