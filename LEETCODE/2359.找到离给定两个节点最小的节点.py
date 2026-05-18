class Solution:
    def closestMeetingNode(self, edges, node1, node2):
        from collections import deque
        n = len(edges)
        def bfs(node):
            vis = [-1]*n
            q = deque([node])
            cnt = 0
            while q:
                x = q.popleft()
                vis[x] = cnt
                y = edges[x]
                if y != -1 and vis[y] == -1:
                    q.append(y)
                cnt += 1
            return vis
        
        list1 = bfs(node1)
        list2 = bfs(node2)
        ans = -1
        mn = float("inf")
        for i in range(n):
            if list1[i] != -1 and list2[i] != -1:
                mx = max(list1[i], list2[i])
                if mx < mn:
                    mn = mx
                    ans = i
        return ans

edges = [4,4,4,5,1,2,2]
node1 = 1
node2 = 1
print(Solution().closestMeetingNode(edges, node1, node2))