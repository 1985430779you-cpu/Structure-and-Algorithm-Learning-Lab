class Solution:
    def typeNum(self, pressedKeys):
        MOD = 1_000_000_007
        short = [1, 2, 3]
        long = [1, 2, 3, 4]
        ans = 1

        s = pressedKeys[0]
        length = 1
        for i in range(1, len(pressedKeys)):
            if pressedKeys[i] == s and i != len(pressedKeys)-1:
                length += 1
            elif pressedKeys[i] != s or i == len(pressedKeys)-1:
                if i == len(pressedKeys)-1 and pressedKeys[i] == pressedKeys[i-1]:
                    length += 1
                if s == "7" or s == "9":
                    selected_list = long
                else:
                    selected_list = short
                record = [0]*(length+1)
                record[0] = 1
                for j in range(1, length+1):
                    for value in selected_list:
                        record[j] += record[j-value] if j-value >= 0 else 0
                ans *= record[length]
                s = pressedKeys[i]
                length = 1
        return ans % MOD
                
pressedKeys = "344644885"
sol = Solution()
print(sol.typeNum(pressedKeys))