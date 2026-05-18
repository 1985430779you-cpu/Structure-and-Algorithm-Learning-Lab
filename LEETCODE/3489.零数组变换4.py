#bfs暴力枚举时间复杂度是指数级的，会超时
class Solution:
    def minZeroArray(self, nums, queries):
        from collections import deque
        import copy
        m = len(queries)
        n = (1 << len(nums)) - 1
        
        q = deque([nums])
        k = 0
        while k < m and q:
            tmp = q
            q = []
            lower, upper, val = queries[k]
            check = (1 << upper+1) - (1 << lower)
            for list in tmp:
                for j in range(n+1):
                    if j & check != j:
                        continue
                    new_list = list.copy()
                    for i in range(len(nums)):
                        if j >> i & 1:
                            new_list[i] -= val
                    if new_list.count(0) == len(nums):
                        return k+1
                    if all(value >= 0 for value in new_list):
                        q.append(new_list)
            k += 1
        return -1
    
class Solution1:
    def minZeroArray(self, nums, queries):
        ans = 0
        for i, x in enumerate(nums):
            if x == 0:
                continue
            dp = [False for _ in range(x+1)]
            dp[0] = True
            for k, (l, r, v) in enumerate(queries):
                if i < l or i > r:
                    continue
                for j in range(x, v-1, -1):
                    dp[j] = dp[j] or dp[j-v]
                if dp[x]:
                    ans = max(ans, k+1)
                    break
            else:
                return -1
        return ans                

nums = [2,0,2]
queries = [[0,2,1],[0,2,1],[1,1,3]]
print(Solution1().minZeroArray(nums, queries))