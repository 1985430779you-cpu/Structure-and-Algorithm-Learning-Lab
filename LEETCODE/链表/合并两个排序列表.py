class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def queue(self, head1, head2):
        if not head1 and not head2:
            return None
        elif not head1:
            return head2
        elif not head2:
            return head1
        
        dummy = ListNode(0)
        cur1, cur2 = head1, head2
        Queue = dummy

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                Queue.next = cur1
                cur1 = cur1.next
            else:
                Queue.next = cur2
                cur2 = cur2.next
            Queue = Queue.next
        #处理cur1或者cur2剩余部分
        if cur1:
            Queue.next = cur1
        else:
            Queue.next = cur2
        
        return dummy.next #Queue已经走到尾端，dummy.next是真正的头节点