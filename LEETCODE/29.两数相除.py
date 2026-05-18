class Solution:
    def divide(self, dividend, divisor):
        quotient = 0
        
        if divisor == 0:
            raise ValueError
        if dividend == 0 and divisor != 0:
            return quotient
        
        if dividend > 0 and divisor > 0:
            while dividend > 0:
                dividend -= divisor
                quotient += 1
            else:
                quotient -= 1
        elif dividend > 0 and divisor < 0:
            while dividend > 0:
                dividend += divisor
                quotient -= 1
            else:
                quotient += 1
        elif dividend < 0 and divisor > 0:
            while dividend < 0:
                dividend += divisor
                quotient -= 1
            else:
                quotient += 1
        elif dividend < 0 and divisor < 0:
            while dividend < 0:
                dividend -= divisor
                quotient += 1
            else:
                quotient -= 1

        if quotient > 2**31 - 1:
            return 2**31 - 1
        elif quotient < -2**31:
            return -2**31
        else:
            return quotient

dividend = 5
divisor = 3
sol = Solution()
try:
    result = sol.divide(dividend, divisor)
    print(result)
except ValueError as e:
    print("ValueError" )