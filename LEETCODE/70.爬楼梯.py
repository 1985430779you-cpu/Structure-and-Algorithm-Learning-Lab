class Solution:
    def climbStairs(self, n):
        if n <= 3:
            return n
        
        f0, f1 = 0, 1
        for _ in range(1, n):
            ans = f0+f1
            f0 = f1
            f1 = ans

        return ans