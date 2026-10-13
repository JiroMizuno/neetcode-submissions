from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        currCon = {}
        long = 0
        for i in nums:
            if i-1 not in currCon.keys():
                currCon[i] = 1
            else:
                currCon[i] = currCon[i-1] + 1
            long = max(long, currCon[i])
        return long