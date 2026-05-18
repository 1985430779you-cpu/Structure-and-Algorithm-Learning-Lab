class Solution:
    def minRemoval(self, nums, k):
        if len(nums) == 1:
            return 0
        nums.sort()
        res, i, maximum = 1, 0, 0
        for j in range(len(nums)-1):
            res = j + 1
            if nums[j+1] /nums[j] > k:
                i += 1
            maximum = max(maximum, len(nums)-(res-i+1))
        return maximum

nums = [4, 6]
k = 2
sol = Solution()
print(sol.minRemoval(nums, k))