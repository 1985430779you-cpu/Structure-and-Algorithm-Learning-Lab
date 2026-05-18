class Solution0:
    def maximumUniqueSubarray(self, nums):
        dic, maximum, i = {}, 0, 0
        for j in range(len(nums)):
            if nums[j] in dic:
                i = max(i, dic[nums[j]] + 1)
            dic[nums[j]] = j
            sum = 0
            for item in nums[i:j+1]:
                sum += item
            maximum = max(maximum, sum)
        return maximum

class Solution:
    def maximumUniqueSubarray(self, nums):
        set0 = set()
        maximum = current = left = 0
        for right in range(len(nums)):    
            while nums[right] in set0:
                set0.remove(nums[left])
                current -= nums[left]
                left += 1
            
            set0.add(nums[right])
            current += nums[right]
            maximum = max(maximum, current)
        return maximum

nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]
sol = Solution()
print(sol.maximumUniqueSubarray(nums))