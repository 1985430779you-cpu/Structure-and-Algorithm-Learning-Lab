class Solution:
    def maxSubarrayLength(self, nums, k):
        n = len(nums)
        if n == 0 or k <= 0:
            return 0
        
        hash = {}
        ans = 0
        i = 0
        for j in range(n):
            if nums[j] not in hash:
                hash[nums[j]] = 1
            else:
                hash[nums[j]] += 1
                while hash[nums[j]] > k:
                    if hash[nums[i]] > 1:
                        hash[nums[i]] -= 1
                    else:
                        del hash[nums[i]]
                    i += 1
            ans = max(ans, j-i+1)
        return ans

s = [1,2,3,1,2,3,1,2]
k = 2
sol = Solution()
print(sol.maxSubarrayLength(s, k))