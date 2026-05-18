class Solution:
    def longestOnes(self, nums, k):
        n = len(nums)
        if n == 0 or k < 0:
            return 0
        
        i = 0
        ans = 0
        for j in range(n):
            if nums[j] == 0:
                k -= 1
                if k < 1:
                    while i <= j and k < 0:
                        if nums[i] == 0:
                            k += 1
                        i += 1           
            ans = max(ans, j-i+1)
        return ans
    
s = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
sol = Solution()
print(sol.longestOnes(s, k))