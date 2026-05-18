class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) == 0:
            return []
          
        n = len(tinput)
        ans, maximum, pop_num = [], 0, 0
        for _ in range(0, n):
            if len(ans) < k:
                ans.append(tinput.pop(0))
            else:
                maximum = max(ans)
                pop_num = tinput.pop(0)
                if maximum >= pop_num:
                    ans.remove(maximum)
                    ans.append(pop_num)
        
        return ans

a = [4,5,1,6,2,7,3,8]
k = 4
sol = Solution()
print(sol.GetLeastNumbers_Solution(a, k))