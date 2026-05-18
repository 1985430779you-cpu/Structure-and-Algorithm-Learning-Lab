class Solution:
    def oddFirst(self, a):
        n = len(a)
        if n == 0 or n == 1:
            return a
        
        odd = []
        even = []
        for num in a:
            if num % 2 == 1:
                odd.append(num)
            else:
                even.append(num)
        
        a.clear()
        a.extend(odd)
        a.extend(even)

        return a

array = [1, 2, 3, 4, 5]
sol = Solution()    
print(sol.oddFirst(array))