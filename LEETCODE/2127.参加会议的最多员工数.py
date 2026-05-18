class Solution:
    def maximumInvitations(self, favorite):
        from collections import deque, defaultdict
        n = len(favorite)
        prev = [0]*n
        r_favorite = [[] for _ in range(n)]
        for i in range(n):
            prev[favorite[i]] += 1
            r_favorite[favorite[i]].append(i)
        
        q = deque([])
        for i in range(n):
            if prev[i] == 0:
                q.append(i)
        while q:
            x = q.popleft()
            y = favorite[x]
            prev[y] -= 1
            if prev[y] == 0:
                q.append(y)

        #最长的环
        dis = list(range(n))
        def find(x):
            if dis[x] != x:
                dis[x] = find(dis[x])
            return dis[x]
        for i in range(n):
            if prev[i] == 1 and prev[favorite[i]] == 1:
                dis[find(i)] = find(favorite[i])
            else:
                dis[i] = -1
        circle = defaultdict(int)
        for i in range(n):
            if dis[i] != -1:
                circle[find(dis[i])] += 1
        
        #特殊情况，2人环对数        
        def bfs(x):
            depth = 0
            q = deque([x])
            while q:
                tmp = q
                q = []
                for x in tmp:
                    for y in r_favorite[x]:
                        if prev[y] == 0:
                            q.append(y)
                depth += 1
            return depth
        
        ans = 0
        vis = [0]*n
        mx = 0
        for i in range(n):
            if vis[i] == 1:
                continue
            vis[i] = 1
            if prev[i] == 1:
                length = circle[find(i)]
                if length > 2:
                    ans = max(ans, length)
                elif length == 2:
                    j = favorite[i]
                    vis[j] = 1
                    depth_i, depth_j = bfs(i), bfs(j)
                    mx += depth_i+depth_j
        ans = max(ans, mx)
        return ans

favorite = [7,0,7,13,11,6,8,5,9,8,9,14,15,7,11,6]
print(Solution().maximumInvitations(favorite))