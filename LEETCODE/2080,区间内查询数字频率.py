#重点复习
class RangeFreqQuery:
    def __init__(self, arr):
        from collections import defaultdict
        pos = defaultdict(list) #普通字典访问不存在的key会报错
        for i in range(len(arr)):
            pos[arr[i]].append(i) #追加，不覆盖
        self.pos = pos

    def query(self, left, right, value):
        a = self.pos[value]
        import bisect
        return bisect.bisect_right(a,right) - bisect.bisect_left(a,left)