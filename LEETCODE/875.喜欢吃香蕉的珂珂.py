class Solution:
    def minEatingSpeed(self, piles, h):
        if h < len(piles):
            return 
        
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low+high) // 2
            total_h = 0
            for i in range(len(piles)):
                total_h += (piles[i]+mid-1) // mid
            if total_h > h:
                low = mid + 1
            else:
                high = mid - 1
        return low
    
piles = [3,6,7,11]
h = 8
sol = Solution()
print(sol.minEatingSpeed(piles, h))