class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        f0 = nums[0]
        f1 = max(nums[1], nums[0])

        for i in range(2, n):
            mx = max(f0+nums[i], f1)
            f0 = f1
            f1 = mx

        return f1
    
nums = [2,7,9,3,1]
sol = Solution()
print(sol.rob(nums))