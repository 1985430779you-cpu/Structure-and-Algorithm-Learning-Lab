class Solution:
    def tallestBillboard(self, rods):
        from functools import cache
        n = len(rods)

        @cache
        def dfs(i, sum):
            if i < 0:
                return 0 if sum == 0 else -float("inf")
            negative = dfs(i-1, sum-rods[i])
            zero = dfs(i-1, sum)
            positive = rods[i] + dfs(i-1, sum+rods[i])
            return max(negative, zero, positive)

        ans = dfs(n-1, 0)
        return ans


rods = [1,2,3,6]
print(Solution().tallestBillboard(rods))