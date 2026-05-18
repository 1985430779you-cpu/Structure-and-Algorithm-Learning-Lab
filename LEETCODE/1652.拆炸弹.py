class Solution:
    def decrypt(self, code, k):
        n = len(code)
        if k == 0:
            code  = [0] * n
            return code
        code = code * 3
        Code, sum = [], 0
        if k > 0:
            for i in range(n+1, 2*n+k):
                sum += code[i]
                left = i - k + 1
                if left < n+1:
                    continue
                else:
                    Code.append(sum)
                    sum -= code[left]
        elif k < 0:
            for i in range(n+k, 2*n-1):
                sum += code[i]
                left = i + k + 1
                if left < n+k:
                    continue
                else:
                    Code.append(sum)
                    sum -= code[left]
        return Code

code = [2, 4, 9, 3]
k = -2
sol = Solution()
print(sol.decrypt(code, k))