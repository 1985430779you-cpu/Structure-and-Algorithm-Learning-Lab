class Solution:
    def maxInWindows(self, a, k):
        n = len(a)
        if n == 0:
            return 0
        list = []
        if n <= 3:
            for i in range(0, n):
                list.append(a[i])
            return list
        
        i = -k
        maximum = []
        while i+k < n:
            if i >= 0:
                list.pop(0)
                list.append(a[i+k])
            else:
                list.append(a[i+k])
                
            if len(list) == k:
                    maximum.append(max(list))
            i += 1

        return maximum
    
a = [2,3,4,2,6,2,5,1]
k = 3
sol = Solution()
print(sol.maxInWindows(a, k))