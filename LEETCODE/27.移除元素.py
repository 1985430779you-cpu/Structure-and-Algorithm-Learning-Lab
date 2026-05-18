import copy
class Solution:
    def removeElement(self, nums, val):
        res = copy.deepcopy(nums)
        for item in nums:
            if item == val:
                res.remove(item)
        return len(res), res

nums = [0, 1, 2, 2, 3, 0, 4, 2]
target = 2
sol = Solution()
k, nums = sol.removeElement(nums, target)
print(k,", nums=", nums)