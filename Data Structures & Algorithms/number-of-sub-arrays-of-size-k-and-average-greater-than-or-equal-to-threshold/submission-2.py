class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        bar = k*threshold
        L = 0
        total = sum(arr[:k])
        if total>=bar:
            count+=1
        for L in range(1, len(arr)-k+1):
            total = sum(arr[L:L+k])
            if total >= bar:
                count += 1
        return count
