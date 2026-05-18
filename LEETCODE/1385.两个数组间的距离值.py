class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        m, n = len(arr1), len(arr2)
        arr2.sort()
        count = 0
        for i in range(m):
            low, high = 0, n-1
            while low <= high:
                mid = (low+high) // 2
                if arr1[i] - arr2[mid] > d:
                    low = mid + 1
                elif arr1[i] - arr2[mid] < -d:
                    high = mid - 1
                else:
                    count += 1
                    break
        return m-count
