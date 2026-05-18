class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def ringStartPoint(self, head):
        #确认链表是否为环形链表
        if not head or not head.next:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        #确认环形链表起始位置
        #fast保持不动，到入口的距离就是a（起始点到入口距离）
        return None
