class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        res = 0
        maxF = 0
        letters = {}
        for R in range(len(s)):
            letters[s[R]] = 1 + letters.get(s[R],0)
            maxF = max(maxF, letters[s[R]])
            if (R - L + 1)- maxF > k:
                letters[s[L]] -= 1
                L += 1
            res = max(res, R-L+1)
        return res





#"XYWXYYYYYYYAY"
#most_common_letter = "Y"
# {X:1, Y:2, W:1}
# rule non-most-common must be <= k


