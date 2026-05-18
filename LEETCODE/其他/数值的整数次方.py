class Solution:
    def Power(self, base, exponent):
        flag = 0
        if base == 0:
            return 0 
        
        if exponent == 0:
            return 1
        
        result = 1
        if exponent < 0:
            flag = 1
            exponent = abs(exponent)
        
        while exponent != 0:
            result *= base
            exponent -= 1

        if flag:
            result = 1 / result

        return result

base = 0
exponent = -3
sol = Solution()
print(sol.Power(base, exponent))