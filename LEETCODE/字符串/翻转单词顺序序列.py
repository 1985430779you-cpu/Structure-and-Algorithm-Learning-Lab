class Solution:
    def reverseSentence(self, s):
        s_list = s.split()
        return " ".join(s_list[::-1])

s = "student. a am I"
sol = Solution()
print(sol.reverseSentence(s))