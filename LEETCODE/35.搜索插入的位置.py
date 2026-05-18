'''
class Solution:
    def searchinsert(self, nums, target):
        if not nums or target <= nums[0]:
            return 0
        elif target == nums[-1]:
            return len(nums)-1
        elif target > nums[-1]:
            return len(nums)
        
        low, high = -1, len(nums)-1
        while low+1 < high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid
            else:
                return mid
            
        if nums[low] < target < nums[high]:
            return low+1
'''
class Solution:
    def searchinsert(self, nums, target):
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

nums = [1, 3, 5, 6, 9, 12]
target = 8
sol = Solution()
print(sol.searchinsert(nums, target))