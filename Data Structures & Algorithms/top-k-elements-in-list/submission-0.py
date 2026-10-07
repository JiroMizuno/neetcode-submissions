from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        nums.sort()
        for i in nums:
            freq[i] += 1    
        ans = sorted(freq.keys(), key=lambda x:freq[x], reverse=True)
        return ans[:k]