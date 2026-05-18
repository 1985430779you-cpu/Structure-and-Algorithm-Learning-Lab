import math
#一维空间复杂度寻找中位数算法
class Solution(object):
    def FindMedian(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        nums1 = [-math.inf] + nums1 + [math.inf]
        nums2 = [-math.inf] + nums2 + [math.inf]
        k = (m + n + 1) // 2

        i, j = 0, k
        while nums1[i+1] <= nums2[j]:
            i += 1
            j -= 1
                
        a1 = max(nums1[i], nums2[j])
        b1 = min(nums1[i+1], nums2[j+1])
        return a1 if (m+n) % 2 else (a1 + b1) / 2
         
nums1 = [1, 2, 7, 9]
nums2 = [2, 3, 4, 5, 6, 8, 10, 11, 12]
sol = Solution()
sol.FindMedian(nums1, nums2)
result = sol.solution()
print(result)