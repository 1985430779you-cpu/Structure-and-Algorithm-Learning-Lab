class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        if n < 2:
            return []
        
        i, j = 0, n-1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]
        
        return []