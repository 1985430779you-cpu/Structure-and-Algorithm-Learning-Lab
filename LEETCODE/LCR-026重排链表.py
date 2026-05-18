class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow
        rev = None

        while cur:
            tmp = cur.next
            cur.next = rev
            rev = cur
            cur = tmp

        first, second = head, rev
        while second.next:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
            
        return head