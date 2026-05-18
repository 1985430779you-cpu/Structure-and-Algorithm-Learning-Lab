class Solution:
    def isNumeric(self, s):
        n = len(s)
        if n == 0:
            return False
        
        # 定义状态标志
        has_dot = False
        has_e = False
        has_digit = False
        i = 0
        
        # 处理可选的正负号
        if s[i] == '+' or s[i] == '-':
            i += 1
        
        # 扫描数字部分
        while i < n and '0' <= s[i] <= '9':
            has_digit = True
            i += 1
        
        # 处理小数点
        if i < n and s[i] == '.':
            has_dot = True
            i += 1
            while i < n and '0' <= s[i] <= '9':
                has_digit = True
                i += 1
        
        # 处理科学计数法 e/E
        if i < n and (s[i] == 'e' or s[i] == 'E'):
            has_e = True
            i += 1
            
            # e/E后面必须有数字
            if i < n and (s[i] == '+' or s[i] == '-'):
                i += 1
            
            e_has_digit = False
            while i < n and '0' <= s[i] <= '9':
                e_has_digit = True
                i += 1
            
            if not e_has_digit:
                return False
        
        # 必须至少有一个数字，并且扫描完整个字符串
        return has_digit and i == n

# 测试
s = ".51E-16"
sol = Solution()
print(sol.isNumeric(s))  # 输出: True