class Solution:
    def minimumTime(self, time, totalTrips):
        left = min(time) - 1
        right = min(time) * totalTrips
        while left <= right:
            mid = (left+right) // 2
            total = sum(mid // time[i] for i in range(len(time)))
            if total >= totalTrips:
                right = mid-1
            else:
                left = mid+1
        
        return left
    
time = [1,2,3]
totalTrips = 5
sol = Solution()
print(sol.minimumTime(time, totalTrips))