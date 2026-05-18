class Solution:
    def floodFill(self, image, sr, sc, color):
        m, n = len(image), len(image[0])
        pos = [[1]*n for _ in range(m)]
        val = image[sr][sc]
        
        def dfs(i, j, val, image):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if image[i][j] != val:
                return
            if pos[i][j] == 0:
                return
            pos[i][j] = 0
            image[i][j] = color
            dfs(i-1,j, val, image)
            dfs(i+1,j, val, image)
            dfs(i,j-1, val, image)
            dfs(i,j+1, val, image)
            return image
        
        image = dfs(sr, sc, val, image)
        return image
    
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
sol = Solution()
print(sol.floodFill(image, sr, sc, color))    