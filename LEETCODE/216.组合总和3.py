class Solution:
    def combinationSum3(self, k: int, n: int):
        List = [i for i in range(1, 10)]
        if n == 1:
            return []
        
        ans = []
        path = []

        def dfs(i, start, sum):
            if i == k:
                if sum == n:
                    ans.append(path[:])
                    return

            for j in range(start, len(List)):
                path.append(List[j])
                dfs(i+1, j+1, sum+List[j])
                path.pop()

        dfs(0, 0, 0)
        return ans
    
k = 3
n = 2
sol = Solution()
print(sol.combinationSum3(k, n))