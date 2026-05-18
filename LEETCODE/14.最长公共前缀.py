class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        if all(item == strs[0] for item in strs):
            return strs[0]
        for i in range(1, len(strs[0])+1):
            string = strs[0][:i]
            for j in range(1, len(strs)):
                if strs[j][0:i] != string:
                    return strs[j][:i-1]
        return strs[0]

strs = ["a", "racecar", "car"]
sol = Solution()
print(sol.longestCommonPrefix(strs))