#异或题目重点复习
class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            temp = num1 ^ num2
            carry = (num1 & num2) << 1

            num1, num2 = temp, carry
        
        return num1
    
a = 5
b = 7
sol = Solution()
print(sol.Add(a, b))