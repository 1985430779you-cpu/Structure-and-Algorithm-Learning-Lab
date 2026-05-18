class Solution:
    def factorial(self, A):
        B = []
        if len(A) == 0:
            return []
        
        from functools import reduce
        for j in range(0, len(A)):
            tmp = A[j]
            A[j] = 1
            B.append(reduce(lambda x, y: x*y, A))
            A[j] = tmp
        
        return B
"""     
        def multiply(result, i, x):
            if i == len(A):
                return result

            if i != x:
                result *= A[i]
            return multiply(result, i+1, x)
        
        for j in range(0, len(A)):
            b = multiply(1, 0, j)
            B.append(b)
            
        return B
""" 

A = [1, 2, 3, 4]
sol = Solution()
print(sol.factorial(A))