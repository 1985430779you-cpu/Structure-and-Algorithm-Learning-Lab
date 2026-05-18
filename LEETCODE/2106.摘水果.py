"""
import random
import copy
class Solution:    
    def maxTotalFruits(self, fruits, startPos, k):
        strawberry, sum = [], 0
    
        def dfs(fruits, pos, step, sum):
            res_fruits = copy.deepcopy(fruits)
            if step == 0:
                strawberry.append(sum)
            else:
                next_step = one direction or left then right or right then left +-1               
                for k, (i, j) in enumerate(fruits):
                    if next_step == i:
                        sum += j
                        res_fruits.pop(k)
                        break
                dfs(res_fruits, next_step, step-1, sum)
        
        dfs(fruits, startPos, k, sum)
        ans = max(strawberry)
    
        return ans
"""
class Solution:    
    def maxTotalFruits(self, fruits, startPos, k):

fruits = [[2,8],[6,3],[8,6]]
startPos = 5
k = 4
sol = Solution()
print(sol.maxTotalFruits(fruits, startPos, k))