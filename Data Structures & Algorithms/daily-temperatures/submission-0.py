class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        outList = []
        for i in range(len(temperatures)):
            count = 0
            found = False
            for g in range(i+1, len(temperatures)):
                count += 1
                if temperatures[i] < temperatures[g]:
                    found = True
                    outList.append(count)
                    break
            if not found:
                outList.append(0)
        return outList

        