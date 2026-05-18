#重点复习:二分法
class Solution:
    def findMin(self, nums):
        n = len(nums)
        i, j = 0, n-1
        while i < j:
            mid = (i+j) // 2
            if  nums[mid] == nums[j]:
                j -= 1
            elif nums[mid] < nums[j]:
                j = mid
            else:
                i = mid+1
        return nums[i]