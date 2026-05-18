class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            if nums[0] >= target:
                return 1
            return 0
        
        i = 0
        min_len = n+1
        sum = 0
        for j in range(n):
            sum += nums[j]
            while sum >= target:
                min_len = min(min_len, j-i+1)
                sum -= nums[i]
                i += 1

        if min_len == n+1:
            return 0
        
        return min_len
