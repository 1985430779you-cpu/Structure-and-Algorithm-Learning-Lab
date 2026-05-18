class Solution:
    def longestValidParentheses(self, s):
        Dict = {")": "(", "}": "{"}
        List, count = [], 0
        for i in range(len(s)):
            if List:
                if Dict.get(s[i]) == List[-1]:
                    List.pop()
                    count += 2
                else:
                    List.append(s[i])
            else:
                List.append(s[i])
        return count
    
s = "((({})"
sol = Solution()
print(sol.longestValidParentheses(s))