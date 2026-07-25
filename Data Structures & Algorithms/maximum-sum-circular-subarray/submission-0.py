class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        start = nums[0]
        currentMax = start
        currentMin = start
        globalMax = start
        globalMin = start
        for num in nums[1:]:
            currentMax = max(num, num + currentMax)
            globalMax = max(currentMax, globalMax)
            currentMin = min(num, num + currentMin)
            globalMin = min(currentMin, globalMin)

        return max(globalMax, sum(nums)-globalMin) if sum(nums) >= 0 else globalMax