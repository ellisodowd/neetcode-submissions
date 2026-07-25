class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        big = nums[0]
        current = nums[0]
        for num in nums[1:]:
            current = max(current + num, num)
            if current > big:
                big = current
        return big