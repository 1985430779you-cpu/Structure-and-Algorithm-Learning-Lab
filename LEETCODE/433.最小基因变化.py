class Solution:
    def minMutation(self, startGene, endGene, bank):
        from collections import deque
        if endGene not in bank:
            return -1
        if startGene not in bank:
            bank.append(startGene)
        n = len(bank)
        g = [[] for _ in range(n)]
        hash = {}
        for i in range(n):
            hash[bank[i]] = i

        for i in range(n):
            for j in range(i+1, n):
                cnt = 0
                for k in range(8):
                    if bank[i][k] != bank[j][k]:
                        cnt += 1
                        if cnt >= 2:
                            break
                if cnt == 1:
                    g[hash[bank[i]]].append(hash[bank[j]])
                    g[hash[bank[j]]].append(hash[bank[i]])
        start = bank.index(startGene)
        end = bank.index(endGene)

        vis = [-1]*n
        vis[start] = 0
        q = deque([start])
        while q:
            x = q.popleft()
            for y in g[x]:
                if vis[y] < 0:
                    vis[y] = vis[x]+1
                    q.append(y)
        return vis[end]        

    
startGene = "AACCGGTT"
endGene = "AAACGGTA" 
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
print(Solution().minMutation(startGene, endGene, bank))