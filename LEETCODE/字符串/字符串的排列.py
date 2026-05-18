class Solution:
    def Permutation(self, a):
        n = len(a)
        if n == 0:
            return []
        
        ans = []
        path = []
        def dfs(i, string):
            if i == n:
                ans.append("".join(path[:]))
                return
            
            for j in range(0, len(string)):
                path.append(string[j])
                dfs(i+1, string[:j] + string[j+1:])
                path.pop()

        dfs(0, a)
        return ans
    
a = "abc"
sol = Solution()
print(sol.Permutation(a))