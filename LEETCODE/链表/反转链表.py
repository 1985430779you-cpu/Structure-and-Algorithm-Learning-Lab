class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
    
class Solution:
    def printListchart(self, head):
        result = []
        while head:
            result.insert(0, head.val)
            head = head.next
        return result
    
    def createListchart(self, result):
        if not result:
            return None
        head = ListNode(result[0])
        cur = head
        for value in result[1:]:
            cur.next = ListNode(value)
            cur = cur.next
