class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        p0 = dummy

        def pnext(node, n):
            cur = node
            for _ in range(0, n):
                if cur is None:
                    return False
                cur = cur.next
            return True

        while pnext(p0.next, k): #p0.next而不是p0，否则tmp.next会报错
            cur = p0.next
            rev = None

            for _ in range(0, k):
                tmp = cur.next
                cur.next = rev
                rev = cur
                cur = tmp

            nxt = p0.next
            p0.next.next = cur
            p0.next = rev
            p0 = nxt

            #for _ in range(0, k):
                #p0 = p0.next

        return dummy.next