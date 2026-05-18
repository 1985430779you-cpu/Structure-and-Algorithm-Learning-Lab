class Solution0: #递归
    def Fibonacci(self, n):
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)
    
class Solution1: #循环
    def Fibonacci(self, n):
        first, second = 0, 1
        for i in range(0, n-1):
            sum = first + second
            first = second
            second = sum

        return sum
    
n = 40
sol = Solution1()
print(sol.Fibonacci(n))