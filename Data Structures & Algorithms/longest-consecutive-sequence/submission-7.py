class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        long = 0
        # turn array into set to count each number once instead
        # if there is no i-1, it's the start so increment until 
        # there is no more and record the sequence number
        for i in numSet:
            lenny = 0
            if i-1 not in numSet:
                lenny+=1
                while i+1 in numSet: 
                    i += 1
                    lenny+=1
                long = max(long, lenny)
        return long