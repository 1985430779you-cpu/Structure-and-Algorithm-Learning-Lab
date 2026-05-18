class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)

        vis = [0]*n
        def dfs(x):
            vis[x] = 1
            for y in rooms[x]:
                if vis[y] == 0:
                    dfs(y)
        
        dfs(0)
        if all(vis[i] == 1 for i in range(n)):
            return True
        return False

rooms = [[1,3],[3,0,1],[2],[0]]
print(Solution().canVisitAllRooms(rooms))     