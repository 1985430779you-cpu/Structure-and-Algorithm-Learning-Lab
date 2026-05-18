class Solution(object):
    def convert(self, s, numRows):
        if numRows < 2: 
            return s
        list = [[] for i in range(numRows)]
        
        j, flag = 0, 1
        for i in range(0, len(s)):
            list[j].append(s[i])
            j += flag
            if j % numRows == 0 and j != 0:
                flag = -1
                j += (2*flag)
            elif j < 0:
                flag = 1
                j += (2*flag)
        
        A = []
        for i in list:
            a = "".join(i)
            A.append(a)
        return "".join(A)

string = "PAYPALISHIRING"
numRows = 3
sol = Solution()
print(sol.convert(string, numRows))