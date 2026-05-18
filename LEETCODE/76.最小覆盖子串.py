class Solution:
    def minWindow(self, s, t):
        m = len(s)

        from collections import Counter
        s_counter = Counter()
        t_counter = Counter(t)

        ans_left, ans_right = -1, m
        left = 0
        for right in range(m):
            if s[right] not in s_counter:
                s_counter[s[right]] = 1
            else:
                s_counter[s[right]] += 1
            while s_counter >= t_counter: #重点复习，字典s涵盖字典t的表示方法
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                s_counter[s[left]] -= 1
                left += 1

        return s[ans_left: ans_right+1] if ans_left != -1 else ""
    
class Solution1:
    def minWindow(self, s, t):
        m, n = len(s), len(t)
        from collections import Counter
        t_counter = Counter(t)
        count = len(t_counter)
        left = 0
        ans_left, ans_right = -1, m
        ans = ""
        for right in range(m):
            if s[right] in t_counter:            
                t_counter[s[right]] -= 1
                if t_counter[s[right]] == 0:
                    count -= 1
            
            while count == 0:
                if right - left <= ans_right - ans_left:
                    ans_left, ans_right = left, right
                    ans = s[ans_left : ans_right+1]

                if s[left] in t_counter:
                    t_counter[s[left]] += 1
                    if t_counter[s[left]] > 0:
                        count += 1
                left += 1
            
        return ans
    
s = "abc"
t = "cba"
sol = Solution()
print(sol.minWindow(s, t))