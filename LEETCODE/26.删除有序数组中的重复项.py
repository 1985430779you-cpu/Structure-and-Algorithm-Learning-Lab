class Solution:
    def removeDuplicates(self, nums):
        res = list(set(nums))
        return len(res), res

nums=[0,0,1,1,1,2,2,3,3,4]
sol = Solution()
k, nums = sol.removeDuplicates(nums)
print(k,", nums=", nums)