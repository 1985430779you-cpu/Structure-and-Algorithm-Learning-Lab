class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def reverse_k(self, head, k):
        if not head or k <= 0:
            return None

        left = right = head
        for i in range(0, k):
            if not right:
                return None
            right = right.next

        while right:
            right = right.next
            left = left.next

        return left