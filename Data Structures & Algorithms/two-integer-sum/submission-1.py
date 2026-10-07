class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summer = {}
        for i in range(len(nums)):
            if nums[i] in summer:
                return [summer[nums[i]], i]
            idx = target - nums[i]
            summer[idx] = i