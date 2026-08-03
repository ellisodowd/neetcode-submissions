class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixL = [1]*n
        prefixR = [1]*n

        for i in range(len(nums)):
            j = n-i-1
            if i == 0:
                prefixL[i] = nums[i]
                prefixR[j] = nums[j]
            else:
                prefixL[i] = prefixL[i-1] * nums[i]
                prefixR[j] = prefixR[j+1] * nums[j]
        result = [0]*n
        print(prefixL,prefixR)
        for i in range(len(nums)):           
            if i == 0:
                result[i] = prefixR[i+1]
            elif i == n-1:
                result[i] = prefixL[i-1]
            else:
                result[i] = prefixL[i-1] * prefixR[i+1]

        return result
        