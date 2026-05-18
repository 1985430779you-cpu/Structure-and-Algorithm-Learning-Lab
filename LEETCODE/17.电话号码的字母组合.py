class Solution:
    def letterCombinations(self, digits:str):
        dict = {"2":"abc", "3":"def",
                "4":"ghi", "5":"jkl",
                "6":"mno", "7":"pqrs",
                "8":"tuv", "9":"wxyz"
                }
   
        res=[]
        def backtrack(combination, nextdigit):
            if len(nextdigit) == 0:
                res.append(combination)
            else:
                for i in dict[nextdigit[0]]:
                    backtrack(combination+i, nextdigit[1:])
        backtrack("", digits)
        return res

digits = "2"
sol = Solution()
print(sol.letterCombinations(digits))