"""
class Solution(object):
    def LengthOfLongestSubstring(self, s):
        self.s = s

    def FindLength(self):
        substring = None
        list = []
        for i in range(0, len(self.s)):
            substring = self.s[i]
            length = 1
            for j in range(i+1, len(self.s)):
                if self.s[j] in substring:
                    list.append(length)
                    break 
                else:
                    substring += self.s[j]
                    length += 1
        return list

def MaxNumberinList(given_list):
    max = given_list[0]
    for i in range(1, len(given_list)):
        if given_list[i] > max:
            max = given_list[i]
    return max
"""
class Solution(object):
    def LengthOfLongestSubstring(self, s):
        if not s:
            return 0
        dict, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dict:
                #不定长滑动窗口的关键代码：字符上一次出现的位置,max确保向左移动
                i = max(i, dict[s[j]])
            dict[s[j]] = j
            res = max(res, j - i)
        return res

String = " "
sol = Solution()
print(sol.LengthOfLongestSubstring(String))