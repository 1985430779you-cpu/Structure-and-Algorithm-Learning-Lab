class Solution(object):
    def maximumLengthSubstring(self, s):
        dic0, res, i, maximum = {}, {}, 0, 0
        for j in range(len(s)):
            if s[j] in dic0:
                if s[j] in res:
                    i = max(i, dic0[s[j]]+1)
                    dic0[s[j]] = res[s[j]]
                res[s[j]] = j
            else:
                dic0[s[j]] = j
            maximum = max(maximum, j-i+1)
        return maximum

String = "aaaa"
sol = Solution()
print(sol.maximumLengthSubstring(String))