class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def deleteRepetition(self, head):
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        cur = dummy
        left = right = head
        right = right.next

        while left:
            if right and left.val == right.val:
                duplicate = left.val
                while left and left.val == duplicate:
                    left = left.next
                    right = right.next if right else None                    
            else:
                cur.next = left
                cur = cur.next
                left = left.next
                right = right.next if right else None

        cur.next = None
        return dummy.next
                