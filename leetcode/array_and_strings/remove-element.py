class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

        # [3, 2, 2, 3]
        # ij
        # [3, 2, 2, 3]
        #  j  i
        # [2, 2, 2, 3]
        #     j  i
        # [2, 2, 2, 3] # the 3 doesnt matter
        #        j  i