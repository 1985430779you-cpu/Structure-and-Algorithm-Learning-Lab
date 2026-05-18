class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        cur = 1
        while cur <= n:
            low = n % cur
            high = n // cur // 10

            if  n // cur % 10 > 1:
                count += (high+1) * cur
            elif n // cur % 10 == 1:
                count += high*cur + (low+1)
            else:
                count += high * cur
            
            cur *= 10

        return count
    
n = 12
sol = Solution()
print(sol.NumberOf1Between1AndN_Solution(n))