class Solution(object):
    def isPalindrome(self,x):
        return str(x) == str(x[::-1])

num = input("input a number:")
sol = Solution()
print(sol.isPalindrome(num))