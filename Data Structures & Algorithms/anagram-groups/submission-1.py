from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaList = []
        anaDict = defaultdict(list)
        for wrd in strs:
            sortWrd = str(sorted(wrd))
            anaDict[sortWrd].append(wrd)
        answer = []
        for i in anaDict.keys():
            answer.append(anaDict[i])
        return answer
            