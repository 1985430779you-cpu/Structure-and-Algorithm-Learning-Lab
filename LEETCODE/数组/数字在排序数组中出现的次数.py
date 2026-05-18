class Solution:
    def findDuplicate(self, a, target):
        n = len(a)
        if n == 0:
            return 0
        
        low, high = 0, n-1

        while low <= high:
            mid = (low + high) // 2
            if a[mid] == target:
                break
            elif a[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        else:
            return 0
        
        left = right = mid
        while left > 0 and a[left-1] == target:
            left -= 1
        while right < n-1 and a[right+1] == target:
            right += 1

        return right-left+1

a = [1, 4, 5, 6, 7, 7, 7, 8, 10, 12]
sol = Solution()
print(sol.findDuplicate(a, 12))