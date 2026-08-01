class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights)-1
        maximum = 0
        while L < R:
            maximum = max(maximum, (R-L)*min(heights[L],heights[R]))
            if heights[L] < heights[R]:
                L+=1
            else:
                R-=1
        return maximum
        

        