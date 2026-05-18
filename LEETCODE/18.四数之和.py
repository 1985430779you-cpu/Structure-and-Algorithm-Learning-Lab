class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        ans = []
        for i in range(0, len(nums)-3):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                l = len(nums)-1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target: #等于的时候要判断是否答案重复
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        l -= 1
                        while l > k and nums[l] == nums[l+1]:
                            l -= 1
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1                        
                    elif sum > target:
                        l -= 1
                    else:
                        k += 1
        return ans 

nums = [2, 2, 2, 2, 2]
target = 8
sol = Solution()
print(sol.fourSum(nums, target))