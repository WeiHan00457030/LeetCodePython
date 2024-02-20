#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
import math
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        sum = 0

        for i in range(len(arr)):
            left,right = 0,0
            for left_index in range(i-1,-1,-1):
                if arr[left_index] > arr[i]:
                    left += 1
                else:
                    break
            for right_index in range(i,len(arr)):
                if arr[right_index] >= arr[i]:
                    right += 1
                else:
                    break

            sum += ((left*right)+right)*arr[i]
        return int(sum%(math.pow(10,9)+7))
# @lc code=end
