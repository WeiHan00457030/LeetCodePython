#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,index = m - 1, n - 1, m + n -1

        # insert from big to small
        while j >= 0:
            if i >=0 and nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i-=1
            else:
                nums1[index] = nums2[j]
                j-=1
            index -=1
        
 
        

# @lc code=end

