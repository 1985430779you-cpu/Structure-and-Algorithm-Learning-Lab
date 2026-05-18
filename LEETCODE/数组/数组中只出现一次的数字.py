""" class Solution:
    def showupOnce(self, a):
        n = len(a)
        if n == 0:
            return []

       counter = {}
        ans = []
        for i in range(n):
            if a[i] not in counter:
                counter[a[i]] = 1
            else:
                counter[a[i]] += 1

        for key, value in counter.items():
            if value < 2:
                ans.append(key)
        
        return ans"""
class Solution: #只出现一次能用异或
    def showupOnce(self, a):
        result = 0
        for num in a:
            result ^= num
        return result
    
a = [2,4,3,6,3,2,5,5]
sol = Solution()
print(sol.showupOnce(a))