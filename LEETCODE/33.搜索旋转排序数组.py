class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums)-1
        mid = (low + high) // 2
        #二分法区分有序数列
        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= nums[high]:
                low = mid + 1
            else:
                high = mid
            rot = low

        #二分法寻找target位置
        low, high = 0, len(nums)-1
        if nums[0] <= target <= nums[rot-1]:
            high = rot-1
        else:
            low = rot

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1
    
nums = [4, 5, 6, 7, 0, 1, 2]
target = 2
sol = Solution()
print(sol.search(nums, target))