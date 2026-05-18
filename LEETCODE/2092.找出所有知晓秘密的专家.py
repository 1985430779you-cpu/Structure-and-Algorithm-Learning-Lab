#并查集优化：0和firstPerson先在一个集合，按时间连不同的集合
class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        meetings = sorted(meetings, key = lambda x: x[2])
        times = {}
        for a, b, c in meetings:
            if c not in times:
                times[c] = []
            times[c].append((a, b))

        def find(x):
            if combine[x] != x:
                combine[x] = find(combine[x])
            return combine[x]

        ans = {0, firstPerson}
        combine = list(range(n))
        combine[firstPerson] = 0
        for time in times:
            check = set()
            for a, b in times[time]:
                check.add(a)
                check.add(b)
                fa, fb = find(a), find(b)
                if fa == 0 or fb == 0:
                    combine[fa] = 0
                    combine[fb] = 0
                elif fa != fb: #已经在集合里，不需要重复合并
                    combine[fa] = fb
            
            for i in list(check):
                if find(i) == 0:
                    ans.add(i)
                if find(i) != 0: #不知道秘密的，重置为指向自身
                    combine[i] = i

        return list(ans)
    
n = 6
meetings = [[1,2,5],[2,3,8],[1,5,10]]
firstPerson = 1
print(Solution().findAllPeople(n, meetings, firstPerson))