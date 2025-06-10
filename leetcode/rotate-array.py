class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # new = {}

        # for i in range(len(nums)):
        #     new[(i + k) % len(nums)] = nums[i] 

        # for i, j in new.items():
        #     nums[i] = j

        # separate solution with slicing
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]