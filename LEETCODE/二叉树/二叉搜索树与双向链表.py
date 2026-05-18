#二叉树转链表，重点复习
class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def treeConvertedIntoNode(self, root):
        if not root:
            return None
        
        self.head = None
        self.tail = None

        def convert(node): #中序排列：左20行，中27行，右28行
            if not node:
                return None
            
            convert(node.left) #遍历左子树
            if self.tail is None: #左子树的最小值首次满足该条件
                self.head = node
            else:
                self.tail.right = node
                node.left = self.tail

            self.tail = node #尾部等于当前节点
            convert(node.right)

        convert(root)
        self.head.left = self.tail
        self.tail.right = self.head
        
        return self.head