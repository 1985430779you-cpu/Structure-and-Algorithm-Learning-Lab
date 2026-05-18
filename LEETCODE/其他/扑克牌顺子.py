class Solution:
    def IsContinuous(self, numbers):
        if len(numbers) != 5:
            return False
        
        list = []
        for num in numbers:
            if num != 0:
                if num not in list:
                    list.append(num)
                else:
                    return False

        if max(list) > 13 or min(list) < 1:
            return False
        
        
        if max(list) - min(list) > 4:
            return False
        
        return True
    
numbers = [12, 0 ,12, 0, 13]
sol = Solution()
print(sol.IsContinuous(numbers))