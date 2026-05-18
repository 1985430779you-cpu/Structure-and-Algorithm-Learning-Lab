class Solution:
    def largestSublist(self, nums, target):
        n = len(nums)
        if target == 0:
            return -1
        if n <= 0:
            return -1
        import math
        record = [-math.inf] * (target+1)
        record[0] = 0
        for x in nums:
            for i in range(target, x-1, -1):
                record[i] = max(record[i],record[i-x]+1)
        
        return record[target] if record[target] > -math.inf else -1
    
nums = [1,1,5,4,5]
target = 3
sol = Solution()
print(sol.largestSublist(nums, target))