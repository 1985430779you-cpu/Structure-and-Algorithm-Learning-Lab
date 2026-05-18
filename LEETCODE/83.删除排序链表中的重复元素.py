class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head
        
        dummy = ListNode(-101)
        dummy.next = head
        left = right = dummy
        right = right.next
        while left.next and right.next:
            val = left.next.val
            if right.next.val == val:
                while right and right.val == val:
                    right = right.next
                left.next = right
            else:
                left = left.next
                right = right.next

        return dummy.next