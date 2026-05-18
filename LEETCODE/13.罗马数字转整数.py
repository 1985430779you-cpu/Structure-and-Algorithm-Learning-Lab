class Solution(object):
    def romanToInt(self, num):
        dict ={"M":1000, "CM":900,
               "D":500, "CD":400,
               "C":100, "XC":90,
               "L":50, "XL":40,
               "X":10, "IX":9,
               "V":5, "IV":4,
               "I":1, "0": 0
                }
        
        i, Sum = 0, 0
        n = len(num)
        while i < n:
            num = num + "0"
            if dict.get(num[i]) < dict.get(num[i+1]):
                Sum = Sum - dict.get(num[i]) + dict.get(num[i+1])
                i += 1
            else:
                Sum += dict.get(num[i])
            i += 1
        return Sum

num = "MCMXCIV"    
sol = Solution()
print(sol.romanToInt(num))