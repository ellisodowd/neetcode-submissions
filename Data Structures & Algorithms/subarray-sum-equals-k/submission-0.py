class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subValues = {0: 1}
        curr = 0
        count = 0
        for num in nums:
            curr += num
            count += subValues.get(curr - k, 0)
            subValues[curr] = subValues.get(curr, 0) + 1
        return count