from collections import Counter
class Solution:
    def moreThanHalfNum0(self, a):
        n = len(a)
        if n == 0:
            return 0
        if n == 1:
            return a[0]
        
        dic = Counter(a)
        num, count = dic.most_common(1)[0] #返回出现次数前n的元素，元素次数
        if count > (n // 2):
            return num
        '''
        for key, value in dic.items():
            if value > (n // 2):
                return key
        '''    
        return 0
    
array = [1,2,3,2,2,2,5,4,2]
sol = Solution()    
print(sol.moreThanHalfNum0(array))