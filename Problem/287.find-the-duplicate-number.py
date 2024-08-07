#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 龜兔賽跑演算法
        # 至少有1重複數字, 代表當所有數字指向下一個index的數字時, 存在循環
        # 龜:每次錢進一步 兔:每次錢進兩步

        hare,tortoise = nums[0],nums[0]

        while True:
            hare = nums[hare]
            tortoise = nums[nums[tortoise]]

            if hare == tortoise:
                break
        
        # 在循環中相遇後,在原點與相遇點已同樣速度前進,相遇處及為循環起點
        ptr1 = nums[0]
        ptr2 = hare
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        
        return ptr1
# @lc code=end

