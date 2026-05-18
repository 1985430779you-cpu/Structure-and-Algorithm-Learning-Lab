class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        ans = []
        path = [0]

        def dfs(x):
            if not graph[x] or x == n-1:
                if x == n-1:
                    ans.append(path[:])
                return
            
            for y in graph[x]:
                path.append(y)
                dfs(y)
                path.pop()

        dfs(0)
        return ans
    
graph = [[2],[],[1]]
print(Solution().allPathsSourceTarget(graph))            