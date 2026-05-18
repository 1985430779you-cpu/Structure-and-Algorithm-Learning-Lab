class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        from collections import defaultdict
        from collections import deque
        n =len(recipes)
        dic = defaultdict(list)
        cnt = defaultdict(int)
        for i in range(n):
            for j in ingredients[i]:
                dic[j].append(recipes[i])
                cnt[recipes[i]] += 1
        
        q = deque([])
        cook = []
        for supply in supplies:
            q.append(supply)
        while q:
            x = q.popleft()
            if x not in supplies:
                cook.append(x)
            for y in dic[x]:
                cnt[y] -= 1
                if cnt[y] == 0:
                    q.append(y)
        return cook

recipes = ["bread","sandwich"]
ingredients = [["yeast","flour"],["bread","meat"]]
supplies = ["yeast","flour","meat"]
print(Solution().findAllRecipes(recipes, ingredients, supplies))