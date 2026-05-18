class Solution:
    def countSubarrays(self, nums, k):
        n = len(nums)
        if n == 0:
            return 0
        
        i, sum = 0, 0
        ans = 0
        for j in range(n):
            sum += nums[j]
            mark = sum * (j-i+1)
            while mark >= k and i <= j:
                sum -= nums[i]
                i += 1
                mark = sum * (j-i+1)
            ans += j-i+1
        return ans
    
nums = [2,1,4,3,5]
k = 10
sol = Solution()
print(sol.countSubarrays(nums, k))