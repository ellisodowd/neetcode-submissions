class Solution:
    def numDecodings(self, s: str) -> int:
        return self.myHelper(s)
        
    def myHelper(self, s):
        if s == "":
            return 1
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        if int(s[:2]) <= 26:
            return self.myHelper(s[2:]) + self.myHelper(s[1:])
        else:
            return self.myHelper(s[1:])
    

    
        
