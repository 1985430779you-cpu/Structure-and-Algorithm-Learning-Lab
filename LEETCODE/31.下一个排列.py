class Solution:
    def nextPermutation(self, nums):
        if len(nums) < 2:
            return nums
        i = len(nums)-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        #先交换两个数字
        if i >= 0:
            j = len(nums)-1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        #交换后，i以后数字全部颠倒
        """
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        """
        nums[i+1:] = nums[i+1:][::-1]
        return nums

nums =[1, 2, 4, 3]
sol = Solution()
print(sol.nextPermutation(nums))