class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        pre = [1]*n
        suf = [1]*n

        # prefix
        for i in range(1, n):
            pre[i] = nums[i-1] * pre[i-1]
        
        # suffix (start at penultimate end, end at idx 0 by decrementing)
        for j in range(n-2, -1, -1):
            suf[j] = nums[j+1] * suf[j+1]
        
        # product of pre + suf
        for k in range(n):
            ans[k] = pre[k] * suf[k]
        
        return ans
        