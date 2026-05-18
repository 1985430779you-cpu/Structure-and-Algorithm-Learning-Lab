class Solution:
    def countSubarrays(self, nums, k):
        n = len(nums)
        if n == 0:
            return 0
        
        maxi = max(nums)
        i = 0
        ans = 0
        count = 0

        for j in range(n):
            if nums[j] == maxi:
                count += 1
            if count == k:
                while count == k:
                    if nums[i] == maxi:
                        count -= 1
                    ans += n-j
                    i += 1
        return ans
    
nums = [1, 3, 2, 3, 3]
k = 2
sol = Solution()
print(sol.countSubarrays(nums, k))