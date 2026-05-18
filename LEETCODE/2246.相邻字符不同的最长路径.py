class Solution: #BFS,但是超时
    def longestPath(self, parent, s):
        hash = {}
        for i in range(len(parent)):
            hash[i] = []
        for i in range(1, len(parent)):
            hash[parent[i]].append(i)
            hash[i].append(parent[i])
        #return hash
        
        mx = 0
        for i in range(len(parent)):
            vis = [1 for _ in range(len(parent))]
            vis[i] = 0
            step = 0            
            q = [i]
            while q:
                tmp = q
                q = []
                for value in tmp:
                    for num in hash[value]:
                        if vis[num] != 0 and s[num] != s[value]:
                            q.append(num)
                            vis[num] = 0
                step += 1
            mx = max(mx, step)
        return mx
    
class Solution1:
    def longestPath(self, parent, s):
        hash = {}
        for i in range(len(parent)):
            hash[i] = []
        for i in range(1, len(parent)):
            hash[parent[i]].append(i)
        
        ans = 0
        def dfs(i):
            nonlocal ans
            len_i = 0
            for j in hash[i]:
                len_j = dfs(j) + 1
                if s[j] != s[i]:
                    ans = max(ans, len_i + len_j)
                    len_i = max(len_i, len_j)
            return len_i
        dfs(0)
        return ans+1
    
parent = [-1,0,0,1,1,2]
s = "abacbe"
print(Solution1().longestPath(parent, s))