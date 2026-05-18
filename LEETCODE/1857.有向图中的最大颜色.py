#重点复习：多功能记忆化搜索
class Solution:
    def largestPathValue(self, colors, edges):
        from collections import defaultdict, deque
        n = len(colors)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)

        cache = [-1]*n
        def dfs(x):
            if cache[x] != -1:
                return cache[x]
            cache[x] = 0
            cnt = defaultdict(int)
            for y in g[x]:
                res = dfs(y)
                if res == 0:
                    return res
                for ch in res: #cnt是x的字典，res是y的字典，cnt从res继承
                    cnt[ch] = max(cnt[ch], res[ch])
            cnt[colors[x]] += 1 #继承后加上本身颜色
            cache[x] = cnt
            return cnt                       
        
        ans = 0
        for i in range(n):
            dict = dfs(i)
            if dict == 0:
                return -1
            ans = max(ans, dict[colors[i]])
        return ans

colors = "hhqhuqhqff"
edges = [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]
print(Solution().largestPathValue(colors, edges))