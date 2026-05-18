class Solution:
    def maximumWhiteTiers(self, tiles, carpetLen):
        maximum, cover, left = 0, 0, 0
        tiles.sort()

        for i, j in tiles:
            cover += j - i + 1
            carpet_left = j - carpetLen + 1

            while carpet_left > tiles[left][0]:
                cover -= tiles[left][1] - tiles[left][0] + 1
                left += 1

            maximum =max(maximum, cover)
        return maximum
    
tiles = [[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]]
carpetLen = 10
sol = Solution()
print(sol.maximumWhiteTiers(tiles, carpetLen))