from collections import defaultdict 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = defaultdict(int)
        freqJ = defaultdict(int)
        for i in s:
            freqS[i] += 1
        for j in t:
            freqJ[j] += 1
        return freqS == freqJ