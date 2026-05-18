class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head):           
        cur = head
        rev = None
        while cur:
            tmp = cur.next
            cur.next = rev
            rev = cur
            cur = tmp
        
        tail = None
        carry = 0
        while rev or carry != 0:
            if rev:
                sum = rev.val*2 + carry
                rev = rev.next
                value = sum % 10
                carry = sum // 10
                dummy = ListNode(value)
            elif not rev and carry != 0:
                dummy = ListNode(carry)
                carry = 0
            dummy.next = tail
            tail = dummy
        return tail        