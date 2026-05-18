class Solution(object):
    def LongestPalindrome(self, s):
        if s == s[::-1]:
            return s
        l = r = 0
        for i in range(len(s)):
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                if right - left - 2 > r - l:
                    l, r = left + 1, right - 1

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 2 > r - l:
                l, r = left + 1, right - 1
        return s[l:r+1]

string = "babad"
sol = Solution()
result = sol.LongestPalindrome(string)
print(result)