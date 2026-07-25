class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = 0
        local_length = 0
        L = 0
        for R in range(len(s)):
            print(L, R)
            if s[R] not in char_set:
                char_set.add(s[R])
                local_length += 1
            else:
                while s[R] in char_set:
                    char_set.remove(s[L])
                    L+=1
                char_set.add(s[R])
                local_length = R-L+1

            max_length = max(max_length, local_length)
        return max_length
        