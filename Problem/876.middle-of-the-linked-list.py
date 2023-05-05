#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break

            slow = slow.next

        return slow
    
    
# @lc code=end

