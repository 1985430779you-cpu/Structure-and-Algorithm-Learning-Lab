class Solution0:
    def PrintMinNumber(self, a):
        n = len(a)
        if n == 0:
            return ""
        if n == 1:
            return a[0]
        
        ans = []
        path = []
        def dfs(i, list):
            if i == n:
                ans.append("".join(path[:]))
                return
            
            for j in range(0, len(list)):
                path.append(list[j])
                dfs(i+1, list[0:j] + list[j+1:])
                path.pop()

        dfs(0, a)
        minimum = min(ans)
        return minimum

class Solution:
    def PrintMinNumber(self, a):
        def sorted_rule(x, y):
            if x + y > y + x: #需要cmp_to_key实现下述功能
                return 1 #1代表x排在y后面
            if x + y < y + x:
                return -1 #-1代表x排在y前面
            else:
                return 0 #0代表顺序不变
        
        from functools import cmp_to_key
        ans = sorted(a, key = cmp_to_key(sorted_rule))
        return "".join(ans)

a = ["3","32","321"]
sol = Solution()
print(sol.PrintMinNumber(a))