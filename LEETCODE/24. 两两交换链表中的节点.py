class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head):
        if not head:
            return head
        
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head
        p0 = dummy

        while n >= 2:
            n -= 2
            cur = p0.next
            rev = None
            for _ in range(2):
                tmp = cur.next
                cur.next = rev
                rev = cur
                cur = tmp

            nxt = p0.next
            p0.next.next = cur
            p0.next = rev
            p0 = nxt
        
        return dummy.next