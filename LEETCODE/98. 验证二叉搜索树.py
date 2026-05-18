class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        
        import math
        left_origin = -math.inf
        right_origin = math.inf

        def recursion(node, left, right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False

            if recursion(node.left, left, node.val) and recursion(node.right, node.val, right):
                return True
            
            return False

        return recursion(root, left_origin, right_origin)