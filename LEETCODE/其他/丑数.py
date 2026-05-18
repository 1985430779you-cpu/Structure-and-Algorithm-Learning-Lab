class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return
        
        if 0 < index <= 6:
            ans = [i for i in range(1, index+1)]
            return ans
        
        ans = [1, 2, 3, 4, 5, 6]
        n, num = 6, 6
        while n < index:
            num += 1
            if num / 2 in ans or num / 3 in ans or num / 5 in ans:
                ans.append(num)
                n += 1

        return ans
    
n = 15
sol = Solution()
print(sol.GetUglyNumber_Solution(n))