#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        originalNext = head.next
        head.next = None
        return Solution.recrusive(head,originalNext)
    def recrusive(head,originalNext):

        tmp = originalNext.next
        originalNext.next = head
        
        if tmp == None:
            return originalNext
        else:
            return Solution.recrusive(originalNext,tmp)
# @lc code=end

