class Solution:
    def FindContinuousSequence(self, tsum):
        ans = []
        i = 1
        j = 2
        while i <= tsum // 2:
            sum = i + j
            path = [i, j]
            while sum <= tsum:
                if sum == tsum:
                    ans.append(path[:])
                    break
                j += 1
                sum += j
                path.append(j)
        
            i += 1
            j = i + 1

        return ans
    
tsum = 100
sol = Solution()
print(sol.FindContinuousSequence(tsum))