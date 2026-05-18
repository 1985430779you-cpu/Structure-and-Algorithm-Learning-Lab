class Solution:
    def maxsum(self, a):
        n = len(a)
        if n == 0:
            return 0
        current_sum, maximum = a[0], a[0]

        for j in range(1, n):
            if current_sum <= 0:
                current_sum = a[j]
            else:
                current_sum += a[j]
            maximum = max(maximum, current_sum)

        return maximum
    
array = [2, -5, -3]
sol = Solution()
print(sol.maxsum(array))