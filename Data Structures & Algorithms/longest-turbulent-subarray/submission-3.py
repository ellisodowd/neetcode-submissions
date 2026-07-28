class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def compare(a, b):
            if a>b:
                return 1
            if a<b:
                return -1
            else:
                return 0
        if len(arr) == 1:
            return 1
        L = 0
        lastNum = arr[0]
        currentComp = 0
        lastComp = None
        maximum = 1
        for R in range(1,len(arr)):
            currentComp = compare(lastNum, arr[R])
            if currentComp == 0:
                L = R
                lastNum = arr[R]
            elif lastComp == currentComp:
                L = R-1
                lastNum = arr[R]
            else:
                maximum = max(maximum, R-L+1)
                lastNum = arr[R]

            lastComp = currentComp
        return maximum