class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dih = {}
        for word in strs:
            temp = ''.join(sorted(word))
            if temp in dih:
                dih[temp].append(word)
            else:
                dih[temp] = [word]
        return list(dih.values())