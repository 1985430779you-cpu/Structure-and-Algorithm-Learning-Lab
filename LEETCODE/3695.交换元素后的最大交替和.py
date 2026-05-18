#查并集，重点复习
class Solution:
    def maxAlternatingSum(self, nums, swaps):
        from collections import defaultdict
        n = len(nums)
        g = [i for i in range(n)]
        
        #查找是否同一集合
        def find(x):
            if g[x] != x:
                g[x] = find(g[x])
            return g[x]

        #同一集合的添加        
        for a, b in swaps:
            g[find(a)] = find(b)
        
        dic = defaultdict(list)
        for i in range(n):
            dic[find(i)].append(i)

        s_total = 0
        for key in dic:
            list1 = []
            negative = 0
            for num in dic[key]:
                list1.append(nums[num])
                if num % 2 == 1:
                    negative += 1
            list1.sort()
            s_total += sum(list1) - 2*sum(list1[i] for i in range(negative))

        return s_total
    
nums = [1,2,3]
swaps = [[0,2],[2,1]]
print(Solution().maxAlternatingSum(nums, swaps))    