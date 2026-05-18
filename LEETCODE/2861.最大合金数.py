#重点复习，开闭区间，<=, <, >, >=对left的处理
class Solution:
    def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
        ans = 0
        mx = min(stock) + budget
        for comp in composition:
            def check(num: int) -> bool:
                money = 0
                for s, base, c in zip(stock, comp, cost):
                    if s < base * num:
                        money += (base * num - s) * c
                        if money > budget:
                            return False
                return True

            left, right = ans, mx
            while left <= right:
                mid = (left + right) // 2
                if check(mid):
                    left = mid + 1
                else:
                    right = mid - 1
            ans = max(ans, left-1)
        return ans