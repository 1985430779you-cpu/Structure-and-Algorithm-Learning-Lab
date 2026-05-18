"""class Solution:
    def Sum_Solution(self, n):
        ans = n
        if ans > 0:
            ans += self.Sum_Solution(n-1)               
        return ans"""
class Solution:
    def Sum_Solution(self, n):
        def summation(i, sum):
            if i >= n:
                return sum
            
            return summation(i+1, sum+i+1)

        return summation(0, 0)
   
n = 100
sol = Solution()
print(sol.Sum_Solution(n))