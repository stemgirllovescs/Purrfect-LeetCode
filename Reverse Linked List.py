 # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # previous, current, then next
        prev = None
        current = head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev
# Space O(1)
# time O(N)