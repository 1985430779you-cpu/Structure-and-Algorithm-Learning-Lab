class Solution:
    def minimizeArrayValue(self, nums):
        def check(limit):
            copy_nums = nums[:]
            for i in range(len(copy_nums)-1, 0, -1):
                if copy_nums[i] > limit:
                    gap = copy_nums[i] - limit
                    copy_nums[i] = limit
                    copy_nums[i-1] += gap

            if copy_nums[0] > limit:
                return False
            return True 

        low, high = min(nums)-1, max(nums)
        while low <= high:
            mid = (low+high) // 2
            if check(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low