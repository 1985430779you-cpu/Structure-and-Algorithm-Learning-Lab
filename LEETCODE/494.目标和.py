class Solution:
    def sumOfObjectives(self, nums, target):
        #正数总和s
        #负数总和sum(nums)-s
        #target = s - (sum(nums)-s)
        #s = (sum(nums)+target) // 2
        s = (sum(nums)+target) // 2
        if abs(target) > sum(nums) or (sum(nums)+target) % 2 == 1:
            return 0
        record = [0] * (s+1)
        record[0] = 1
        for x in nums:
            for j in range(s,x-1,-1):
                record[j] = record[j] + record[j-x]
        return record[-1]

nums = [1]
target = 1
sol = Solution()
print(sol.sumOfObjectives(nums, target))