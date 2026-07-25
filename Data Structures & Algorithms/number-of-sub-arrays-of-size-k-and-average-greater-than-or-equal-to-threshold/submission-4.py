class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        L, R = 0, k
        for i in range(len(arr)-k+1):
            total = sum(arr[L:R])
            av = total/k
            if av >= threshold:
                count += 1
            L, R = L+1, R+1
        return count
