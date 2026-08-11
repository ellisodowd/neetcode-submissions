# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next:
            return head.val + head.next.val
        regular = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                regular = regular.next
        middle = regular.next

        prev = None
        while middle is not None:
            next_node = middle.next
            middle.next = prev
            prev = middle
            middle = next_node
        maximum = 0
        left = head
        right = prev
        maximum = 0
        while right:
            maximum = max(left.val + right.val, maximum)
            left = left.next
            right = right.next
        return maximum