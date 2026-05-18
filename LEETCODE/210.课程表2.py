class Solution:
    def findOrder(self, numCourses, prerequisites):
        from collections import deque
        g = [[] for _ in range(numCourses)]
        prev = [0]*numCourses
        for i, j in prerequisites:
            g[j].append(i)
            prev[i] += 1        
        q = deque([])
        for i in range(numCourses):
            if prev[i] == 0:
                q.append(i)
        ans = []

        while q:
            x = q.popleft()
            ans.append(x)
            for y in g[x]:
                prev[y] -= 1
                if prev[y] == 0:
                    q.append(y)
        
        if len(ans) < numCourses:
            return []
        return ans

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().findOrder(numCourses, prerequisites))