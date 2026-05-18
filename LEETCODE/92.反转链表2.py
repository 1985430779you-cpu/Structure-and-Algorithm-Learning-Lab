class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
    
class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        p0 = dummy

        for _ in range(0, left-1):
            p0 = p0.next

        rev = None
        cur = p0.next
        for _ in range(0, right-left+1):
            tmp = cur.next
            cur.next = rev
            rev = cur
            cur = tmp
        
        p0.next.next = cur
        p0.next = rev 

        return dummy.next