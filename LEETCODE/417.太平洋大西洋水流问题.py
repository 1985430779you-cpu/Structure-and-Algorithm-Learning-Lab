class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        Pacific, Atlantic = set(), set()

        def dfs(i, j, vis):
            if (i, j) in vis:
                return
            vis.add((i, j))
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
                    dfs(x, y, vis)
        
        Pacific_range = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
        Atlantic_range = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]
        for i, j in Pacific_range:
            dfs(i, j, Pacific)
        for i, j in Atlantic_range:
            dfs(i, j, Atlantic)
        ans = Pacific & Atlantic  
        return [list(item) for item in ans]
    
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
sol = Solution()
print(sol.pacificAtlantic(heights))