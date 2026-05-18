class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def lastNumInLoop(self, head, m):
        if m < 1:
            return -1
        
        if m == 1:
            cur = head
            while cur.next != head:
                cur = cur.next
            return cur.val
        
        cur = head
        while cur.next != cur:
            for _ in range(0, m-2):
                cur = cur.next

            cur.next = cur.next.next
            cur = cur.next

        return cur.val
    
if __name__=='__main__':
    A1 = ListNode(0)
    A2 = ListNode(1)
    A3 = ListNode(2)
    A4 = ListNode(3)
    A5 = ListNode(4)
    A6 = ListNode(5)

    A1.next = A2
    A2.next = A3
    A3.next = A4
    A4.next = A5
    A5.next = A6
    A6.next = A1

    m = 1
    sol = Solution()
    print(sol.lastNumInLoop(A1, m))