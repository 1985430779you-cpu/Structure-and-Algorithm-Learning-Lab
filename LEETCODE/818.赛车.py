#无限大的路面或者网格，在用哈希表的时候，要想办法优化/剪枝
class Solution:
    def racecar(self, target):
        from collections import defaultdict
        from heapq import heappop, heappush 
        dict = defaultdict(lambda: float("inf"))
        dict[(0, 1)] = 0 
        h = [(0, 0, 1)]
        
        while h:
            c, x, s = heappop(h)
            if c > dict[(x, s)]:
                continue
            if x == target:
                return c
            if x > 2 * target or x < -target:
                continue
            for nxt_x, nxt_s in (x+s, 2*s), (x, -s/abs(s)):
                nxt_c = c+1
                if nxt_c < dict[(nxt_x, nxt_s)]:
                    dict[(nxt_x, nxt_s)] = nxt_c
                    heappush(h, (nxt_c, nxt_x, nxt_s))

class Solution1:
    def racecar(self, target: int) -> int:
        dp = [float('inf')] * (target + 1)
        dp[0] = 0
        
        for i in range(1, target + 1):
            #直接加速到或超过i，然后反向
            k = 1
            pos = (1 << k) - 1
            
            while pos < i:
                for j in range(k):
                    reverse_pos = pos - ((1 << j) - 1)
                    dp[i] = min(dp[i], k + 1 + j + 1 + dp[i - reverse_pos])
                k += 1
                pos = (1 << k) - 1
                
            # 刚好到达i
            if pos == i:
                dp[i] = min(dp[i], k)
            else:
            # 超过i，然后反向
                dp[i] = min(dp[i], k + 1 + dp[pos - i])
                
        return dp[target] 

target = 2
print(Solution().racecar(target))