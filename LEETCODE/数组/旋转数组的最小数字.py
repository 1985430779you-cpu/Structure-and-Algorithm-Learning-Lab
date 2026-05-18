class Solution:
    def findMin(self, a):
        n = len(a)
        if n == 0:
            return 0
        if n == 1:
            return a[0]
        
        low = 0
        high = n - 1
        while low < high:
            mid = (low + high) // 2
            if a[mid] >= a[0]:
                low = mid + 1
            else:
                high = mid

        return a[low]

array = [3]
sol = Solution()    
print(sol.findMin(array))