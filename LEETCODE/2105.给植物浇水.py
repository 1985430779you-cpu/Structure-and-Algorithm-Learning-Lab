class Solution:
    def minimumRefill(self, plants, capacityA, capacityB):
        n = len(plants)
        count = 0
        left, right = 0, n-1
        left_res, right_res = capacityA, capacityB

        while left <= right:
            if left == right:
                if left_res >= right_res:
                    if left_res < plants[left]:
                        count += 1
                else:
                    if right_res < plants[right]:
                        count += 1
                break

            if left_res < plants[left]:
                count += 1
                left_res = capacityA
            left_res -= plants[left]
            left += 1

            if right_res < plants[right]:
                count += 1
                right_res = capacityB
            right_res -= plants[right]
            right -= 1

        return count 