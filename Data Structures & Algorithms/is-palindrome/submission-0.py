class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        text = "".join(filter(str.isalnum, s))
        R = len(text)-1
        while R>L:
            if str.lower(text[R]) != str.lower(text[L]):
                return False
            L+=1
            R-=1
        return True