#特殊情况：固定最长边
class Solution:
    def triangleNumber(self, nums):
        if len(nums) < 3:
            return 0
        
        nums.sort()
        count = 0
        for k in range(2, len(nums)):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j-i
                    j -= 1
                else:
                    i += 1
        return count