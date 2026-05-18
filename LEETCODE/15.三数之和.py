class Solution:
    def threeSum(self, nums):
        nums.sort()
        if len(nums) < 3:
            return []
        
        ans = []
        i = 0
        if nums[i] > 0:
            return []
        
        while i < len(nums)-2:
            if i >= 1 and nums[i] == nums[i-1]:
                i += 1
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
            i += 1

        return ans

nums = [0]
sol = Solution()
print(sol.threeSum(nums))