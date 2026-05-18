class Solution:
    def countOperation(self, nums):
        count = 0
        while nums:
            if nums[0] != min(nums):
                nums = nums[1:] + nums[0:1]
            else:
                nums.pop(0)
            count += 1
        return count

nums = [3, 4, -1]
sol = Solution()
print(sol.countOperation(nums)) 