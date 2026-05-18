"""
from collections import Counter
class Solution:
    def minArrivalsToDiscard(self, arrivals, w, m):
        checklist = []
        count = i = 0
        n = len(arrivals)
        while i < n:
            if not checklist:
                checklist.append(arrivals[i])
                i += 1
                continue
            checklist.append(arrivals[i])
            counter0 = Counter(checklist)
            if counter0[arrivals[i]] > m:
                checklist[-1] = ""
                arrivals[i] = ""
                count += 1     
            left = i - w + 1
            if left >= 0:
                checklist.pop(0)
            i += 1
        return count
"""
class Solution:
    def minArrivalsToDiscard(self, arrivals, w, m):
        cnt = [0] * (max(arrivals) + 1)
        ans = 0
        for i, x in enumerate(arrivals):
            if cnt[x] == m:
                arrivals[i] = 0
                ans += 1
            else:
                cnt[x] += 1  
            left = i - w + 1
            if left >= 0:
                cnt[arrivals[left]] -= 1
        return ans
    
arrivals = [1, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4]
w = 3
m = 2
sol = Solution()
print(sol.minArrivalsToDiscard(arrivals, w, m))