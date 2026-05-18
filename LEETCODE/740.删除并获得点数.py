class Solution:
    def rob(self, nums):
        n = len(nums) 
        if n <= 1:
            return nums[0]
        f0 = f1 = 0
        for i in range(n):
            f0, f1 = f1, max(f1, f0+nums[i])
        return f1

    def deleteAndEarn(self, nums):
        nums.sort()
        a = nums[0]
        operate = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == a:
                operate[-1] += a
            else:
                if nums[i] != a+1:
                    operate.append(0)
                a = nums[i]
                operate.append(a)
        
        ans = self.rob(operate)
        return ans
    
nums = [3, 4, 2]
sol = Solution()
print(sol.deleteAndEarn(nums))