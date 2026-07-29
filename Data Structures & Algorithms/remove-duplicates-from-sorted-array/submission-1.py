class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        R = len(nums)-1
        hashset = set()
        lastSeen = None
        while R >= 0:
            if nums[R] != lastSeen:
                k+=1
                lastSeen = nums[R]
            else:
                del nums[R]
            R-=1
        return k