class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        def reverseListnode(head):
            cur = head
            rev = None
            while cur:
                tmp = cur.next
                cur.next = rev
                rev = cur
                cur = tmp
            return rev
        
        l1 = reverseListnode(l1)
        l2 = reverseListnode(l2)
        l3 = None
        carry = 0
        while l1 or l2 or carry != 0:
            if l1 or l2:
                if not l1:
                    sum = l2.val + carry
                    l2 = l2.next
                elif not l2:
                    sum = l1.val + carry
                    l1 = l1.next
                else:
                    sum = l1.val + l2.val + carry
                    l1 = l1.next
                    l2 = l2.next
                value = sum % 10
                carry = sum // 10
                dummy = ListNode(value)
            elif not l1 and not l2 and carry != 0:
                dummy = ListNode(carry)
                carry = 0
            dummy.next = l3
            l3 = dummy
        return l3