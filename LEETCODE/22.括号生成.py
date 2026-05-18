"""复杂方法，不推荐使用
import copy
class Solution:
    def generateParenthesis(self, n):
        if n == 0: return [""]
        parenthesis0 = ["("]*n
        set0 = set()
        def backtrack(parenthesis, num):
            if num == 0:
                set0.add(tuple(parenthesis))
            else:
                for cur in range(0, len(parenthesis)):
                    parenthesis1 = copy.deepcopy(parenthesis)
                    parenthesis1.insert(cur+1, ")")
                    backtrack(parenthesis1, num-1)
        backtrack(parenthesis0, n)
        res = []
        for item in set0:
            res.append("".join(list(item)))
        char = copy.deepcopy(res)
        for item in res:
            left, right = 0, 0
            for i in range(0,len(item)):
                if item[i] == "(":
                    left += 1
                elif item[i] == ")":
                    right += 1
                if right>left:
                    char.remove(item)
                    break
        return char

num = 3
sol = Solution()
print(sol.generateParenthesis(num))
"""
class Solution0:
    def generateParenthesis(self, n):
        result = []
        def backtrack(combination, open_count, close_count):
            if len(combination) == 2 * n:
                result.append(''.join(combination))
                return
                       
            if open_count < n:
                combination.append('(')
                backtrack(combination, open_count + 1, close_count)
                combination.pop()
            
            if close_count < open_count:
                combination.append(')')
                backtrack(combination, open_count, close_count + 1)
                combination.pop()
        
        backtrack([], 0, 0)
        return result
    
class Solution:
    def generateParenthesis(self, n):
        if n <= 0:
            return []

        ans = []
        path = []
        def dfs(left, right):
            if left == n and right == n:
                ans.append("".join(path[:]))
                return

            if left < n:
                path.append("(")
                dfs(left+1, right)
                path.pop()   

            if right < left:
                path.append(")")
                dfs(left, right+1)
                path.pop() 

        dfs(0, 0)
        return ans        

num = 3
sol = Solution()
print(sol.generateParenthesis(num))