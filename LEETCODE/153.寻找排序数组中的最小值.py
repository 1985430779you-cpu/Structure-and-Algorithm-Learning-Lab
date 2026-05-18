class Solution:
    def findMin(self, nums):
        n = len(nums)
        i, j = 0, n-2
        while i <= j:
            mid = (i+j) // 2
            if nums[mid] < nums[-1]:
                j = mid-1
            else:
                i = mid+1
        return nums[i]