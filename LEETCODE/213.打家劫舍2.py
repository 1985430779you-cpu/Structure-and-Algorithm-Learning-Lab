class Solution:
    def pick(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        f0 = f1 = 0
        for i in range(n):
            mx = max(f1, f0+nums[i])
            f0 = f1
            f1 = mx
        return f1
    
    def rob(self, nums):
        return max(nums[0] + self.pick(nums[2:len(nums)-1]), self.pick(nums[1:]))