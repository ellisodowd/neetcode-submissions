class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[0]
        slow = nums[0]
        secondSlow = nums[0]
        fast = nums[nums[fast]]
        slow = nums[slow]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        while secondSlow != slow:
            slow = nums[slow]
            secondSlow = nums[secondSlow]
        return secondSlow
