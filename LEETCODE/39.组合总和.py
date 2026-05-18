class Solution:
    def findSum(self, candidates, target):
        res = []
        def backtrack(list, next, start):
            if next == target:
                res.append(list)
            elif next < target:
                for i in range(start, len(candidates)):
                    backtrack(list + [candidates[i]], next + candidates[i], i)
            else:
                return
    
        backtrack([], 0, 0)
        return res

candidates = [2, 3, 6, 7]
target = 7
sol = Solution()
print(sol.findSum(candidates, target))