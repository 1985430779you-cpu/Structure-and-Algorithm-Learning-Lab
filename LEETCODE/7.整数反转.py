class Solution(object):
    def reverse(self, x):
        if x >=0:
            a = int(str(x)[::-1])
        else:
            x = str(abs(x))[::-1]
            a = -int(x)
        if -2**31 <= a <= 2**31 - 1:
            return a
        return 0

num = 0
sol = Solution()
string = sol.reverse(num)
print(string)