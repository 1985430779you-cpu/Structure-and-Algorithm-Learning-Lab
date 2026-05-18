class Solution:
    def strStr(self, haystack, needle):
        length = len(needle)
        for i in range(0, len(haystack)-length+1):
            if haystack[i:i+length] == needle:
                return i
        else:
            return -1

haystack = "butadbutad"
needle = "sad"
sol = Solution()
print(sol.strStr(haystack, needle))