#子集型回溯
class Solution:
    def partition(self, s):
        n = len(s)
        if n == 0:
            return []
        
        ans = []
        path = []
        def dfs(i):
            if i == n: #边界
                ans.append(path[:])
                return
            
            for j in range(i, n):
                t = s[i:j+1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j+1)
                    path.pop()
        
        dfs(0)
        return ans

s = "aab"
sol = Solution()
print(sol.partition(s))
