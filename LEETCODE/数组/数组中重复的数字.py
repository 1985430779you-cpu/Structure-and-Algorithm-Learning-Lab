class Solution:
    def randomDuplicate(self, a):
        if len(a) == 0:
            return None
        hash = set()
        duplicate = []
        for value in a:
            if value not in hash:
                hash.add(value)
            else:
                if value not in duplicate:
                    duplicate.append(value)
        import random
        if not duplicate:
            return None
        else:
            return random.choice(duplicate)
    
a = [2,3,1,0,2,5,3]
sol = Solution()
print(sol.randomDuplicate(a))