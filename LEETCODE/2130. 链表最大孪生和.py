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

        mx = 0
        while head2:
            mx = max(mx, head.val + head2.val)
            head = head.next
            head2 = head2.next
        return mx