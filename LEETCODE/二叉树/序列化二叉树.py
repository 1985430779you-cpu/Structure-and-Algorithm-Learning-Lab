import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preOrder(self, root):
        if not root:
            return []
        
        result = []
        def dfs(root):
            if not root:
                result.append(None)
                return

            result.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return result
    
    def revPreOrder(self, root):
        result = self.preOrder(root)
        result_copy = result.copy()
        
        def build_tree(result):
            if not result:
                return None
            
            val = result.pop(0)
            if val is None:
                return None
            
            node = TreeNode(val)
            node.left = build_tree(result)
            node.right = build_tree(result)

            return node
        
        return build_tree(result_copy) 
    
if __name__=='__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    A6 = TreeNode(6)
 
    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A3.left = A6

    sol = Solution()
    result = sol.preOrder(A1)
    print(result, end = "\n")
    result1 = sol.revPreOrder(A1)
    print(result1, end = "\n")