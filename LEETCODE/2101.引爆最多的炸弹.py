class Solution:
    def maximumDetonation(self, bombs):
        n = len(bombs)
        g = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2 <= bombs[i][2]**2:
                    g[i].append(j)
        
        def dfs(x):
            vis[x] = 1
            s = 1
            for y in g[x]:
                if vis[y] == 0:
                    s += dfs(y)
            return s
        
        ans = 0
        for i in range(n):
            vis = [0]*n
            s = dfs(i)
            ans = max(s, ans)

        return ans
    
bombs = [[1,1,100000],[100000,100000,1]]
print(Solution().maximumDetonation(bombs))    