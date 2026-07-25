class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        bar = threshold*k
        total = sum(arr[:k])
        if total >= bar:
            count += 1
        for L in range(1,len(arr)-k+1):
            total += arr[L+k-1] - arr[L-1]
            if total >= bar:
                count += 1
        return count
