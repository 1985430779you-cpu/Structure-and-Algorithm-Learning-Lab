class Solution(object):
    def intToRoman(self, num):
        dict ={"M":1000, "CM":900,
               "D":500, "CD":400,
               "C":100, "XC":90,
               "L":50, "XL":40,
               "X":10, "IX":9,
               "V":5, "IV":4,
               "I":1
                }
        
        list = []
        for key in dict:
            a = dict.get(key)
            while num >= a:
                num -= a
                list.append(key)
            if num == 0:
                break
        return list

number = 3749
sol = Solution()
list = sol.intToRoman(number)
roman = "".join(list)
print(roman)