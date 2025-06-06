class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = dict()

        for i in range(len(nums)):
            if nums[i] in targets:
                return [i, targets[nums[i]]]
            else:
                targets[target - nums[i]] = i