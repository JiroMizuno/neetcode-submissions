class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        prod = 1
        oneZero = False
        prodNonZero = 1 
        for i in nums:
            prod *= i
            if i == 0:
                if oneZero:
                    return [0] * len(nums)
                oneZero = True
            else:
                prodNonZero *= i
        print(prodNonZero)
        for j in range(len(nums)):
            if nums[j] == 0:
                ans[j] = prodNonZero
            else:
                ans[j] = prod//nums[j]
        
        return ans
            