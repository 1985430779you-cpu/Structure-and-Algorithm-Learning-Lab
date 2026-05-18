class Solution:
    def remainingMethods(self, n, k, invocations):
        g = [[] for _ in range(n)]
        for invocation in invocations:
            g[invocation[0]].append(invocation[1])
        vis = set()       
        def dfs(x):
            vis.add(x)
            for y in g[x]:
                if y not in vis:
                    dfs(y)
        dfs(k)
        ans = [i for i in range(n) if i not in vis]
        for node in invocations:
            if node[0] not in vis and node[1] in vis:
                return [i for i in range(n)]
        return ans
                
n = 4
k = 1
invocations = [[1,2],[0,1],[3,2]]
print(Solution().remainingMethods(n, k, invocations))