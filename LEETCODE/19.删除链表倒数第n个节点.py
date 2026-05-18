class Solution:
    def __init__(self, value):
        self.val = value
        self.next = None

def createNode(node, value):
    cur = node
    while cur.next is not None:
        cur = cur.next
    cur.next = Solution(value)

def printNode(root):
    cur = root
    list = []
    while cur is not None:
        list.append(cur.val)
        cur = cur.next
    print(list)

def removeNthFromEnd(head, n):
    dummy = Solution(0)
    dummy.next = head
    left = right = dummy
    for i in range(0, n+1):
        right = right.next
    while right is not None:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next

head = [1, 2, 3, 4, 5]
n = 2
root = Solution(head[0])
for i in range(1, len(head)):
    createNode(root, head[i])
printNode(root)
removeNthFromEnd(root, n)
printNode(root)