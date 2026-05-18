class Solution:
    def shortestBeatifulSubstring(self, s, k):
        left, right, count, list = 0, 0, 0, []
        List, ans = [], []
        mini = len(s)

        while right < len(s):
            if s[right] == "1":
                count += 1
                list.append(right)

            if count == k:
                List.append(s[left:right+1])
            elif count > k:
                list.pop(-1)
                list.pop(0)
                left = list[0]
                right -= 1
                count -= 2

            right += 1
        
        if not List:
            return ""

        for item in List:
            mini = min(mini, len(item))

        for item in List:
            if len(item) == mini:
                ans.append(item)
        ans.sort()

        return ans[0]

s = "11000111"
k = 1
sol = Solution()
print(sol.shortestBeatifulSubstring(s, k))
