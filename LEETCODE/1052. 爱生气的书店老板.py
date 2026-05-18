import numpy as np
import copy
class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):
        custom = np.asarray(customers).reshape(1, len(customers))
        maximum = 0
        for i in grumpy:
            if i: i = 0
            else: i = 1
        grumpy0 = copy.deepcopy(grumpy)
        for i in range(len(grumpy)):
            grumpy[i] = 1
            left = i - minutes +1
            if left <= 0:
                continue
            grumpy[left] = grumpy0[left]
            grum = np.asarray(grumpy).reshape(len(customers), 1)
            k = np.dot(custom, grum)
            maximum = max(k[0][0], maximum)
        return maximum

customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
sol = Solution()
print(sol.maxSatisfied(customers, grumpy, minutes))