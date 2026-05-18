class Solution:
    def jumpFloor(self, number):
        jump = [i for i in range(1, number+1)]
        if number == 1:
            return 1
        
        ans = []
        path = []
        def dfs(sum):
            if sum == number:
                ans.append(path[:])
            elif sum < number:
                for j in jump:
                    path.append(j)
                    dfs(sum+j)
                    path.pop()

        dfs(0)
        return len(ans)
    
n = 7
sol = Solution()
print(sol.jumpFloor(n))