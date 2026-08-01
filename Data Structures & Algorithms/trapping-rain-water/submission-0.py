class Solution:
    def trap(self, height: List[int]) -> int:
        leftHighest = 0
        rightHighest = 0
        n = len(height)
        LMax = [None]*n
        RMax = [None]*n
        #compute prefixes
        for i in range(n):
            j = n-1-i
            leftHighest = max(leftHighest, height[i])
            LMax[i] = leftHighest

            rightHighest = max(rightHighest, height[j])
            RMax[j] = rightHighest

        waterCount = 0
        for i in range(n):
            water = min(LMax[i], RMax[i])-height[i]
            waterCount += max(0, water)
        return waterCount

        