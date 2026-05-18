#heapq堆题，重点复习
class MedianFinder:
    def __init__(self):
        self.left = []  # 入堆的元素取相反数，变成最大堆
        self.right = []

    def addNum(self, num):
        import heapq
        if len(self.left) == len(self.right):
            heapq.heappush(self.left, -heapq.heappushpop(self.right, num))
        else:
             heapq.heappush(self.right, -heapq.heappushpop(self.left, -num))

    def findMedian(self):
        import heapq
        if len(self.left) == len(self.right):
            return (self.right[0] - self.left[0]) / 2
        else:
            return -self.left[0]