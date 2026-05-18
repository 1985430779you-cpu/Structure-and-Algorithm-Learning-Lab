class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        set1 = set()
        def backtrack(sum, list1, candidate):
            if sum == target:
                set1.add(tuple(list1))
            elif sum > target:
                return
            else:
                for i, item in enumerate(candidate):
                    new_candidates = candidate.copy()[i+1:]
                    backtrack(sum + item, list1 + [item], new_candidates)

        backtrack(0, [], candidates)
        res = []
        for item in set1:
            res.append(list(item))
        return res
    
candidates = [2, 5, 2, 1, 2]
target = 8
sol = Solution()
print(sol.combinationSum2(candidates, target))