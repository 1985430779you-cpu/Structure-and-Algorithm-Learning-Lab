class Solution:
    def FirstAppearingOnce(self, s):
        n = len(s)
        if n <= 0:
            return ""
        
        dic = {}
        for i in range(0, n):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

        for key, value in dic.items():
            if value == 1:
                return key
            
        return ""
    
s = "google"
sol = Solution()
print(sol.FirstAppearingOnce(s))