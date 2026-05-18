class Solution:
    def rectCover(self, number):
        if number < 1:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        
        first, second, sum = 1, 2, 2  # f(1)=1, f(2)=2
        for i in range(3, number + 1):
            sum = first + second
            first, second = second, sum

        return sum
        
"""        list = [(0, 2), (1, 1), (2, 0)]

        ans = set()
        path = []
        def dfs(first, second, path):
            if first == number and second == number:
                tuple_path = tuple(sorted(path))
                ans.add(tuple_path)
                return
            
            if first > number or second > number:
                return

            for i, j in list:
                dfs(first+i, second+j, path + [(i, j)])

        dfs(0, 0, [])
        return len(ans)"""
    
number = 5
sol = Solution()
print(sol.rectCover(number))