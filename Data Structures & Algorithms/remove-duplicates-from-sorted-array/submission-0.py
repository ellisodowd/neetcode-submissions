class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        R = len(nums)-1
        hashset = set()
        while R >= 0:
            if nums[R] not in hashset:
                k+=1
                hashset.add(nums[R])
            else:
                del nums[R]
            R-=1
        return k