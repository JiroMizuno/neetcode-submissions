from collections import defaultdict 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        freqS = defaultdict(int)
        freqJ = defaultdict(int)
        for i in s:
            freqS[i] += 1
        for j in t:
            freqJ[j] += 1
        return freqS == freqJ