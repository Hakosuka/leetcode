class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_nums = {}
        for index, num in enumerate(nums):
            if target - num in checked_nums:
                return [checked_nums[target-num], index]
            checked_nums[num] = index
                
