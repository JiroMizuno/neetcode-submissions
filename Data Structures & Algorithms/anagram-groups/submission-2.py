from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaList = []
        anaDict = defaultdict(list)
        for wrd in strs:
            sortWrd = str(sorted(wrd))
            anaDict[sortWrd].append(wrd)
        return list(anaDict.values())
            