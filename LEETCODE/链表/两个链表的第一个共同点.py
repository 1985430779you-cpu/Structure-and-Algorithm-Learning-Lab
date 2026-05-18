class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def findFirstComb(self, head1, head2):
        if not head1 or not head2:
            return None
        #head1拼接head2，head2拼接head1
        cur1 = head1
        cur2 = head2
        while cur1 != cur2:
            if cur1 != None:
                cur1 = cur1.next
            else:
                cur1 = head2

            if cur2 != None:
                cur2 = cur2.next
            else:
                cur2 = head1

        return cur1
