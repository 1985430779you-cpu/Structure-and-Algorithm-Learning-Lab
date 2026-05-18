#指针中的困难题
class Solution:
    def trap(self, height):
        #左边最大高度和右边最大高度的最小值，减去当前地块高度，等于该地块能蓄水的数量
        n = len(height)
        
        maxi, pre, post = 0, [], []
        for i in range(0, n):
            maxi = max(maxi, height[i])
            pre.append(maxi)

        maxi = 0
        for j in range(n-1, -1, -1):
            maxi = max(maxi, height[j])
            post.append(maxi)
        post = post[::-1]

        sum = 0
        for num in range(0, n):
            sum += min(pre[num], post[num]) - height[num]
        return sum