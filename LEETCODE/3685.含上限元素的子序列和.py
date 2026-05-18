#重点复习，优化
#n次01背包会超时
class Solution:
    def subsequenceSumAfterCapping(self, nums, k):
        n = len(nums)
        ans = [False for _ in range(n+1)]
        for x in range(1, n+1):
            dp = [False for _ in range(k+1)]
            dp[0] = True
            for value in nums:
                for j in range(k, min(value, x)-1, -1):
                    dp[j] = dp[j] or dp[j-min(value, x)]
            if dp[k]:
                ans[x] = True
        return ans[1:]
    
class Solution1:
    def subsequenceSumAfterCapping(self, nums, k):
        nums.sort()
        n = len(nums)
        ans = [False for _ in range(n)]
        dp = [False for _ in range(k+1)]
        dp[0] = True

        i = 0
        for x in range(1, n+1):
            #先处理<=x的情况，>x的先用来判断，但不处理
            while i < n and nums[i] == x:
                for j in range(k, x-1, -1):
                    dp[j] = dp[j] or dp[j-x]
                i += 1

            for j in range(min(n-i, k//x)+1):
                if dp[k-j*x]:
                    ans[x-1] = True
                    break
        return ans
    
nums = [4,3,2,4]
k = 5
print(Solution1().subsequenceSumAfterCapping(nums, k))