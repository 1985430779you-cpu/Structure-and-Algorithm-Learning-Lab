class Solution:
    def isValid(self, s):
        if len(s) % 2 == 1: return False
        dict = {")":"(", "]":"[", "}":"{"}
        stack = []
        for i in s:
            if i in dict:
                if stack and stack[-1] == dict[i]:
                    stack.pop()
                else: break
            else:
                stack.append(i)
        return not stack
    
s = "({[]})"
sol = Solution()
print(sol.isValid(s))