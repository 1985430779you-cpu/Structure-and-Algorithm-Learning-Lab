class Solution:
    def jumpFloor(self, number):
        jump = [1, 2]
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
        return ans
    
n = 4
sol = Solution()
print(sol.jumpFloor(n))