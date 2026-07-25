class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        R = 1
        total = nums[L]
        shortest_length = float('inf')
        if total >= target:
            return 1
        while R<len(nums):
            if total < target:
                total += nums[R]
                R += 1
            while total >= target:
                shortest_length = min(shortest_length, R-L)
                total -= nums[L]
                L+=1
        return 0 if shortest_length == float('inf') else shortest_length
