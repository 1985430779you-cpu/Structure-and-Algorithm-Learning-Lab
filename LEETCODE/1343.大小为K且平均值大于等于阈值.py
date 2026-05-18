class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        if k > len(arr):
            return ValueError
        sum = count = 0
        for i, j in enumerate(arr):
            sum += j
            left = i - k + 1
            if left < 0:
                continue
            if sum / k >= threshold:
                count += 1
            sum -= arr[left]
        return count

arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
k = 3
threshold = 5
try:    
    sol = Solution()
    print(sol.numOfSubarrays(arr, k, threshold))
except ValueError:
    print("ValueError")