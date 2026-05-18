class Solution:
    def countPairs(self, nums, target):
        n = len(nums)
        if n < 2:
            return 0
        
        nums.sort()
        count = 0
        for i in range(n-1):
            j = n-1
            while i < j:
                if nums[i] + nums[j] >= target:
                    j -= 1
                else:
                    count += j-i
                    break
        return count
    
nums = [-1,1,2,3,1]
target = 2
sol = Solution()
print(sol.countPairs(nums, target))