import math
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        Cloest, min, Cloestnum = 0, math.inf, 0
        if len(nums) <= 3:
            for i in nums:
                Cloest += i
            return Cloest
        
        for k in range(0, len(nums)-2):
            i, j = k+1, len(nums)-1
            while i<j:
                Sum = nums[k] + nums[i] + nums[j]
                cloest = abs(Sum - target)
                if cloest < min:
                    min = cloest
                    Cloestnum = Sum
                if Sum < target:
                    i += 1
                elif Sum > target:
                    j -= 1
                else:
                    return target
        return Cloestnum

nums = [-1, 2, 1, -4]
target = 1    
sol = Solution()
print(sol.threeSumClosest(nums, target))