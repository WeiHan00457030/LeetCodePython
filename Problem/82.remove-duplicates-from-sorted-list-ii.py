#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return None

        dummy = ListNode(0,head)

        prev,cur = dummy,head

        duplication = -101

        while cur.next:
            if cur.val == cur.next.val:
                duplication = cur.val
            
            if cur.val == duplication:
                prev.next = cur.next
            else:
                prev = prev.next

            cur = cur.next
        
        if cur.val == duplication:
            prev.next = None
        
        return dummy.next
# @lc code=end

