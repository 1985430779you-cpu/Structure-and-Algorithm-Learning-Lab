class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        if not root:
            return None
        
        ans = []
        from collections import deque
        Q = deque([root])
        while Q:
            vals = []
            n = len(Q)
            for _ in range(0, n):
                q = Q.popleft()
                vals.append(q.val)
                if q.left: Q.append(q.left)
                if q.right: Q.append(q.right)

            ans.append(vals)    

        return ans[-1][0]