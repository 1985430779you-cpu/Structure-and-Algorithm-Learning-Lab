class Solution(object):
    def maxArea(self, height):
        maxArea = 0
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                Area = (j-i) * min(height[i], height[j])
                if Area > maxArea:
                    maxArea = Area
        return maxArea
    
Height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
sol = Solution()
print(sol.maxArea(Height))