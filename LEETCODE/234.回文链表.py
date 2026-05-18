class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        left = right = head
        while right and right.next:
            left = left.next
            right = right.next.next
        
        cur = left
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        head2 = prev

        while head2:
            if head.val == head2.val:
                head = head.next
                head2 = head2.next
            else:
                return False
        return True