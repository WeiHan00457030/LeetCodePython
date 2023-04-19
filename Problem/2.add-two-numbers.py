#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        carry,sum = 0,0
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            sum += carry

            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            
            
            cur.next = ListNode(sum)
            cur = cur.next
        
        if carry:
            cur.next = ListNode(carry)
            
        return dummy.next
                
                
# @lc code=end

