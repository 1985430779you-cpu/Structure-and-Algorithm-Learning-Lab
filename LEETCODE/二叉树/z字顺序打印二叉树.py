class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zPrint(self, root):
        if not root:
            return ""

        string = ""
        result, queue, tmp, depth = [root], [], [], 0
        while result: #bfs
            while result:
                cur = result.pop(0)
                queue.append(cur.val)
                if cur.left: tmp.append(cur.left)
                if cur.right: tmp.append(cur.right)
            
            while queue:
                if depth % 2 == 0:
                    a = queue.pop(0)
                else:
                    a = queue.pop(-1)
                string += str(a) + " "
            
            string += "\n"
            result = tmp
            queue, tmp =[], []
            depth += 1 
        
        return string

if __name__=='__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    A6 = TreeNode(6)
    A7 = TreeNode(7)
 
    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A3.right = A7
    A4.left = A6

    sol = Solution()
    print(sol.zPrint(A1))