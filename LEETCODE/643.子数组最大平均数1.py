class Solution:
    def findMaxAverage(self, nums, k):
        if len(nums) < k:
            raise ValueError
        sum = avg = 0
        for i, j in enumerate(nums):
            sum += j
            left = i - k + 1
            if left < 0:
                continue
            avg = max(avg, sum/k)
            sum -= nums[left]
        return avg

nums = [1, 12, -5, -6, 50, 3]
k = 6
try:    
    sol = Solution()
    print(sol.findMaxAverage(nums, k))
except ValueError:
    print("ValueError")