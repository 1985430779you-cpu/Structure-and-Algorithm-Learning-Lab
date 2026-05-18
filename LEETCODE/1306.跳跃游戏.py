class Solution:
    def canReach(self, arr, start):
        n = len(arr)
        g = [[] for _ in range(n)]
        for i in range(n):
            if arr[i] == 0:
                continue
            if 0 <= i+arr[i] < n:
                g[i].append(i+arr[i])
            if 0 <= i-arr[i] < n:
                g[i].append(i-arr[i])
        
        vis = [0]*n
        def dfs(x):
            if arr[x] == 0:
                return True
            vis[x] = 1
            for y in g[x]:
                if vis[y] == 0:
                    if dfs(y):
                        return True
            return False
        
        return dfs(start)

arr = [3,0,2,1,2]
start = 2
print(Solution().canReach(arr, start))                