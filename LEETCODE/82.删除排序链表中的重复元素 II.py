class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            if cur.next.next.val == cur.next.val:
                value = cur.next.val
                while cur.next and cur.next.val == value:
                    cur.next = cur.next.next
            else:
                cur = cur.next           

        return dummy.next