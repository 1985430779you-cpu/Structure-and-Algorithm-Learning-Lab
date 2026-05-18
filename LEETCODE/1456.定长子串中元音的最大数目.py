'''
#O(nk)
class Solution:
    def maxVowels(self, s, k):
        List = ["a", "e", "i", "o", "u"]
        maximum = 0
        for i in range(len(s)-k):
            string = s[i: i+k]
            count = 0
            for j in range(len(string)):
                if string[j] in List:
                    count += 1
            else:
                maximum = max(count, maximum)
        return maximum
'''
#O(n)
class Solution:
    def maxVowels(self, s, k):
        List = ["a", "e", "i", "o", "u"]
        maximum = count = 0
        for i, j in enumerate(s):
            if j in List:
                count += 1
            left = i - k + 1
            if left < 0:
                continue
            maximum = max(count, maximum)
            if maximum == k:
                break
            if s[left] in List:
                count -= 1
        return maximum

s = "tryhard"
k = 4
sol = Solution()
print(sol.maxVowels(s, k))