import re
class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()
        a = re.findall(r"^[\+\-]?\d+", s)
        #正则表达式：^[\+\-]?表示开头为+或者-，+和-出现0-1次
        #正则表达式：\d+ 代表一个或者多个数字
        num = int(*a)
        return max(-2**31, min(num, 2**31 - 1))

string = "word and 987"
sol = Solution()
print(sol.myAtoi(string))