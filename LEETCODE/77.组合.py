#
class Solution:
    def combine(self, n: int, k: int):
        list = [i for i in range(1, n+1)]
        length = len(list)

        ans = []
        path = []
        def dfs(i, start):
            if i == k:
                ans.append(path[:])
                return
            
            for j in range(start, n):
                path.append(list[j])
                dfs(i+1, j+1)
                path.pop()

        
        dfs(0, 0)
        return ans
    
n = 4
k = 2
sol = Solution()
print(sol.combine(n, k))