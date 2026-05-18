class Solution:
    def listStrip(self, nums):
        n = len(nums)
        if n <= 0:
            return True
        if n == 1:
            return False
        if sum(nums) % 2 == 1:
            return False
        import math
        s = sum(nums) // 2
        record = [math.inf] * (s+1)
        record[0] = 0
        for x in nums:
            for j in range(s,x-1,-1):
                record[j] = min(record[j], record[j-x]+1)
        
        return True if record[-1] < math.inf else False

nums = [1, 1, 11, 9]
sol = Solution()
print(sol.listStrip(nums))        