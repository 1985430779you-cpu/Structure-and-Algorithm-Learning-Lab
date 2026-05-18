class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        from collections import deque
        ans = []
        Q = deque([root])
        count = 0

        while Q:
            vals = []
            n = len(Q)            
            for _ in range(0, n):
                if count % 2 == 0:
                    q = Q.popleft()
                    if q.left:
                        Q.append(q.left)
                    if q.right:
                        Q.append(q.right)
                else:
                    q = Q.pop()
                    if q.right:
                        Q.appendleft(q.right)
                    if q.left:
                        Q.appendleft(q.left)
                vals.append(q.val)

            count += 1            
            ans.append(vals)

        return ans