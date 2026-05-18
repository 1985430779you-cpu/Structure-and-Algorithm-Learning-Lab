class Solution0:
    def sumofCombination(self, nums, target):
        record = [0]*(target+1)
        record[0] = 1
        for j in range(1, target+1):
            for i in nums:
                record[j] += record[j-i] if j-i>=0 else 0       
        return record[-1]

class Solution:
    def sumofCombination(self, nums, target):
        n = len(nums)
        if n == 0:
            return 0

        path = []
        ans = []
        def dfs(sum): 
            if sum == 0:
                ans.append(path[:])
                return
            elif sum < 0:
                return
            
            for value in nums:
                path.append(value)
                dfs(sum-value)
                path.pop()
        
        dfs(target)
        return len(ans)

nums = [1, 2, 3]
target = 4
sol = Solution0()
print(sol.sumofCombination(nums, target))            