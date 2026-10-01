from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        freqDict = defaultdict(int)
        wow = False
        for i in nums:
            freqDict[i] += 1
            if freqDict[i] > 1:
                wow = True
                break
        return wow
