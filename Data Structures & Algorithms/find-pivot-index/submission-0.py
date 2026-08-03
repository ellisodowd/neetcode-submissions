class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        num = 0
        n = len(nums)    
        prefixL = [0]*n
        prefixR = [0]*n
        for i in range(len(nums)):
            j = n-i-1
            if i==0:
                prefixL[i] = nums[0]
                prefixR[j] = nums[j]
            else:
                prefixL[i]=prefixL[i-1]+nums[i]
                prefixR[j] = prefixR[j+1]+nums[j]
        #now have prefix sums ready to go
        L = 0
        for i in range(n):
            if prefixL[i] == prefixR[i]:
                return i
        return -1

        