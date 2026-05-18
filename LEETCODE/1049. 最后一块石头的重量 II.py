class Solution:
    def lastStoneWeightII(self, stones):
        s = sum(stones)
        target = s // 2

        def dynamicProgramming(num):
            dp = [False]*(num+1)
            dp[0] = True
            for x in stones:
                for j in range(num, x-1, -1):
                    dp[j] = dp[j] or dp[j-x]
            return dp[num]

        ans = s
        for num in range(1, target+1):
            if dynamicProgramming(num):
                ans = min(ans, abs((s-num)-num))
        return ans
    
class Solution1:
    def lastStoneWeightII(self, stones):
        s = sum(stones)
        target = s // 2
        dp = [False]*(target+1)
        dp[0] = True

        for x in stones:
            for j in range(target, x-1, -1):
                dp[j] = dp[j] or dp[j-x]

        ans = s
        for num in range(1, target+1):
            if dp[num]:
                ans = min(ans, abs((s-num)-num))
        return ans

stones = [31,26,33,21,40]
print(Solution1().lastStoneWeightII(stones))