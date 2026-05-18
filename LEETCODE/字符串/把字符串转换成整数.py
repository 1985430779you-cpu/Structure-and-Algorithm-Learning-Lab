class Solution:
    def strToInt(self, s):
        n = len(s)
        if n == 0:
            return 0
        
        minus = False
        flag = False
        
        if s[0] == "+":
            flag = True
        elif s[0] == "-":
            minus = True
            flag = True

        start = 0
        if flag:
            start = 1

        nums = 0
        for i in range(start, n):
            if "0" <= s[i] <= "9":
                nums = nums*10 + ord(s[i]) - ord("0")
            else:
                return 0
        
        if minus:
            nums *= -1

        return nums

s = "-167"
sol = Solution()
print(sol.strToInt(s))