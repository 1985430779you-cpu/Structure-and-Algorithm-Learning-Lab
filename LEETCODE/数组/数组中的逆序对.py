#基础困难题目，重点复习
class Solution:
    def findInverse(self, a):
        n = len(a)
        if n == 0:
            return 0

        def dfs(merged):
            if len(merged) <= 1:
                return merged, 0
            
            mid = (len(merged)) // 2
            if len(merged) > 1:
                left_arr, left_count = dfs(merged[:mid])
                right_arr, right_count = dfs(merged[mid:])

            merged = [] #拼接left和right中的元素
            count = left_count + right_count

            i = j = 0 #以下保证merged左右两边都为正序排列
            while i < len(left_arr) or j < len(right_arr):
                if i == len(left_arr):
                    merged.append(right_arr[j])
                    j += 1
                    continue
                if j == len(right_arr):
                    merged.append(left_arr[i])
                    i += 1
                    continue

                if left_arr[i] < right_arr[j]:
                    merged.append(left_arr[i])
                    i += 1
                elif left_arr[i] > right_arr[j]:
                    merged.append(right_arr[j])
                    j += 1
                    count += (len(left_arr) - i)

            return merged, count        

        _, count = dfs(a)
        return count
    
a = [5, 4, 3, 2, 1]
sol = Solution()
print(sol.findInverse(a))