#三色标记法
class Solution:
    def canFinish(self, numCourses, prerequisites):
        g = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            g[prerequisites[i][1]].append(prerequisites[i][0])
        
        vis = [0]*numCourses
        def dfs(x):
            vis[x] = 1
            for y in g[x]:
                #等于1有环，等于2往下递归看看是否有环
                if vis[y] == 1 or vis[y] == 0 and dfs(y):
                    return True
            vis[x] = 2
            return False
        
        for i in range(numCourses):
            if vis[i] == 0 and dfs(i):
                    return False     
        return True
    
class Solution1:
    def canFinish(self, numCourses, prerequisites):
        from collections import deque
        g = [[] for _ in range(numCourses)]
        prev = [0]*(numCourses)
        for x, y in prerequisites:
            g[y].append(x)
            prev[x] += 1
        
        q = deque([])
        for i in range(numCourses):
            if prev[i] == 0:
                q.append(i)
        
        while q:
            tmp = q
            q = []
            for x in tmp:
                for y in g[x]:
                    prev[y] -= 1
                    if prev[y] == 0:
                        q.append(y)

        if all(i == 0 for i in prev):
            return True
        return False

numCourses = 5 
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
print(Solution1().canFinish(numCourses, prerequisites))    