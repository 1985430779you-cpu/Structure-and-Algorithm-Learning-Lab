class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        n = len(nums)
        if n == 0:
            return 0
        
        count = 0
        i = 0
        Pi = 1
        for j in range(n):
            Pi *= nums[j]
            while Pi >= k and i <=j:
                Pi /= nums[i]
                i += 1
            count += j-i+1

        return count
