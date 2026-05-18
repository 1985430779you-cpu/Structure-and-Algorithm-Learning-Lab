#创建链表
class NewNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def CreateNode(node, data):
    cur = node
    while cur.next is not None:
        cur = cur.next
    cur.next = NewNode(data)

def PrintNode(head):
    cur = head
    while cur is not None:
        print(cur.val, end = " ")
        cur = cur.next

#链表求和函数
def Sum_with_carry(list1, list2):
    dummy = NewNode(0)
    current = dummy
    carry = 0
    while list1 is not None or list2 is not None or carry !=0:
        val1 = list1.val if list1 else 0
        val2 = list2.val if list2 else 0
        sum = val1 + val2 + carry
        carry = sum // 10
        digit = sum % 10
        current.next = NewNode(digit)
        current = current.next
        if list1 is not None: 
            list1 = list1.next
        if list2 is not None: 
            list2 = list2.next
    return dummy.next

#生成l1链表    
l1 = [9,9,9,9,9,9,9]
Root1 = NewNode(l1[0])
for i in range(1, len(l1)):
    CreateNode(Root1, l1[i])
print("List of l1:")
PrintNode(Root1)

#生成l2链表
l2 = [9,9,9,9]
Root2 = NewNode(l2[0])
for i in range(1, len(l2)):
    CreateNode(Root2, l2[i])
print("\nList of l2:")
PrintNode(Root2)

#相加链表
result = Sum_with_carry(Root1, Root2)
print("\nresult:")
PrintNode(result)