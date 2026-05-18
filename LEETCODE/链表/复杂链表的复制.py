class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.random = None

class Solution:
    def copyComplexListChart(self, head):
        #复制复杂链表
        cur = head
        while cur:
            copy = ListNode(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next #跳两格
            
        #关联复制的链表的的随机指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next #跳两格

        #拆分链表
        dummy = ListNode(0) #哑节点
        Copy = dummy
        cur = head
        while cur:
            Copy.next = cur.next
            Copy = Copy.next            
            cur.next = cur.next.next
            cur = cur.next

        return dummy.next
