class Solution:
    def totalFruit(self, fruits):
        dic, list, i, maximum = {}, [], 0, 0
        for j in range(len(fruits)):
            if j not in dic:
                list.append(fruits[j])
            dic[fruits[j]] = j
            if len(dic) > 2:
                i = dic[list[0]] + 1
                del dic[list[0]]
                list.pop(0)
            maximum = max(maximum, j - i + 1)
        return maximum
    
fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
sol = Solution()
print(sol.totalFruit(fruits))