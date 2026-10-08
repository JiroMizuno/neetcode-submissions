class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        suf = [1]*n

        oneZero = False

        
        # prefix
        for i in range(1, n):
            # zero check
            if nums[i-1] == 0:
                if oneZero:
                    return [0]*n
                oneZero = True

            pre[i] = nums[i-1] * pre[i-1]
        
        # one last check
        if oneZero and nums[n-1] == 0:
            return [0]*n

        # suffix (start at penultimate end, end at idx 0 by decrementing)
        for j in range(n-2, -1, -1):
            suf[j] = nums[j+1] * suf[j+1]
        
        ans = [1]*n
        # product of pre + suf
        for k in range(n):
            ans[k] = pre[k] * suf[k]
        
        return ans
        