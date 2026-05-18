class Solution:
    def maximumTastiness(self, price, k):
        price.sort()
        def findGap(mid):
            a = price[0]
            count = 1
            for i in range(1, len(price)):
                if price[i] - a >= mid:
                    a = price[i]
                    count += 1
            if count >= k:
                return True
            return False

        left, right = 0, price[-1] - price[0]
        while left <= right:
            mid = (left+right) // 2
            if findGap(mid):
                left = mid + 1            
            else:
                right = mid - 1
        return left-1