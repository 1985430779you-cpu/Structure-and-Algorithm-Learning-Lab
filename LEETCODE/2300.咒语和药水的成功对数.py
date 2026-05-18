class Solution:
    def successfulPairs(self, spells, potions, success):
        m, n = len(spells), len(potions)
        if n == 0:
            return []
        
        ans = []
        potions.sort()
        for i in range(m):
            low, high = 0, n-1
            while low <= high:
                mid = (low+high) // 2
                if spells[i] * potions[mid] >= success:
                    high = mid - 1
                else:
                    low = mid + 1
            ans.append[n-low]

        return ans
