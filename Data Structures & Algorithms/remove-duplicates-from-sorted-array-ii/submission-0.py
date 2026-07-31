class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        last = nums[0]
        k = 0
        current_num = nums[L]
        current_count = 1
        for R in range(1,len(nums)):
            if nums[R] == current_num:
                current_count += 1
            else:
                current_num = nums[R]
                current_count = 1
            if current_count <= 2:
                L+=1
                k = L+1
            nums[L] = nums[R]
        return k


        