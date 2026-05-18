class Solution:
    def minFlips(self, mat):
        m, n = len(mat), len(mat[0])
        record = set()
        s = 0
        for i in range(m):
           for j in range(n):
                s += mat[i][j] << (i*n + j)
        q = [s]
        record.add(s)

        cnt = 0
        while q:
            tmp = q
            q = []
            for element in tmp:
                if element == 0:
                    return cnt 
                for i in range(m*n):
                    new_element = element ^ (1 << i)
                    x = i // n
                    y = i % n
                    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                        X, Y = x+dx, y+dy
                        if 0 <= X < m and 0 <= Y < n:
                            new_element ^= (1 << (X*n+Y))
                    if new_element not in record:
                        q.append(new_element)
                        record.add(new_element)
            cnt += 1
        return -1
                
mat = [[0,0],[0,1]]
print(Solution().minFlips(mat))