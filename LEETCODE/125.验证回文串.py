class Solution:
    def isPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return True
        
        left = 0
        right = n-1
        
        while left < right:
            while left < right and not ("a" <= s[left] <= "z" or "A" <= s[left] <= "Z" or "0" <= s[left] <= "9"):
                left += 1
            while left < right and not ("a" <= s[right] <= "z" or "A" <= s[right] <= "Z" or "0" <= s[right] <= "9"):
                right -= 1
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
            
        return True