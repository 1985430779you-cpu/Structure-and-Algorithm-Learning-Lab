class Solution:
    def NumberOf1(self, n):
        n = str(bin(n & 0xffffffff))
       
        count = 0
        for i in range(len(n)):
           if n[i] == "1":
               count += 1

        return count
        
n = -8
sol = Solution()
print(sol.NumberOf1(n))