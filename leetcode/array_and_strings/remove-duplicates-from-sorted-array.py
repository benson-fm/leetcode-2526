class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        # ! (incorrect) can automatically be done by converting to a set then a list
        """
        nums = list(set(nums)) # this makes a copy of another var nums
        return len(nums)
        """

        # two pointer solution
        # j at the beginning
        # i moving
        # if both i != j, j + 1 = i & j += 1

        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1