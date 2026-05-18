class Solution:
    def maxFrequency(self, nums, k):
        if len(nums) == 1:
            return 1
        
        nums.sort()
        i, maximum = 0, 1
        for j in range(1, len(nums)):
            count, record = 1, i
            k_operate = k
            while i < j:
                gap = nums[j] - nums[i]
                i += 1
                k_operate -= gap
                if k_operate < 0:
                    i = record + 1
                    count = j - i + 1
                    break
                count += 1
            else:
                i = record
            maximum = max(maximum, count)
        
        return maximum
#根据数学简化    
class Solution1:
    def maxFrequency(self, nums, k):
        nums.sort()
        left = 0
        total_ops = 0
        max_freq = 1
        
        for right in range(1, len(nums)):
            # 计算新增的操作数
            total_ops += (nums[right] - nums[right - 1]) * (right - left)
            
            # 调整左边界
            while total_ops > k:
                total_ops -= (nums[right] - nums[left])
                left += 1
            
            max_freq = max(max_freq, right - left + 1)
        
        return max_freq
    
nums = [1, 4, 8, 13]
k = 5
sol = Solution1()
print(sol.maxFrequency(nums, k))