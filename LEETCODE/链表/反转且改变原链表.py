class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class solution:    
    def reverse(self, head):
        if not head:
            return None
        cur = head
        rev = None
        #三指正，tmp暂时存储cur后的链表，cur当前指向rev，rev等于目前的cur
        #最后cur从tmp拿回剩余链表，重复操作至cur为空
        while cur:
            tmp = cur.next
            cur.next = rev
            rev = cur
            cur = tmp
        
        return rev
