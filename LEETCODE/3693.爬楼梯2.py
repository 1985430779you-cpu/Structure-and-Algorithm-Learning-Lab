class Solution:
    def climbStairs(self, n, costs):
        total, cost = 0, 0
        step = [1, 2, 3]
        ans = []
        def dfs(total, cost):
            if total == n:
                ans.append(cost)
                return
            else:
                for i in step:
                    if total+i-1 <= len(costs)-1:          
                        dfs(total+i, cost+costs[total+i-1]+i**2)
        
        dfs(total, cost)
        return min(ans)

class Solution1:
    def climbStairs(self, n, costs):
        f0 = f1 = f2 =0
        for cost in costs:
            f0, f1, f2 = f1, f2, min(f0+9, f1+4, f2+1) + cost
        return f2

n = 4
costs = [1,2,3,4]
sol = Solution1()
print(sol.climbStairs(n, costs))