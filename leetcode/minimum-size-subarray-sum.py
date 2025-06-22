class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # base case 

        if sum(nums) < target:
            return 0 

        # sliding window problem
        # we continously grow the right pointer out
        # until we reach the value we want 
        # if it exceeds, try to minimize the window by increase left
        # this the whole checking mechanism where the current sum 
        # if it's smaller
            # increase left
        # if its greater
            # compare between l and right and see if that's smallest
            # increase right
        # we continue to do this until the end 
        # O(n) time, O(1) memory
        # min_dis = float('inf')
        # i = 0
        # j = 0
        # cur_sum = nums[i]
        # while i < len(nums) and j < len(nums):
        #     if i == j:
        #         if nums[i] >= target:
        #             return 1 
        #         elif nums[i] < target:
        #             j += 1
        #             if j < len(nums):
        #                 cur_sum += nums[j]
        #     elif cur_sum >= target:
        #         min_dis = min(min_dis, j - i + 1)
        #         cur_sum -= nums[i]
        #         i += 1 
        #     else:
        #         j += 1
        #         if j < len(nums):
        #             cur_sum += nums[j]
        # return min_dis

        # another way to implement this is to have a nested while loop in a for loop
        
        # better way for implementation
        min_dis = float('inf')
        l = 0
        cur_sum = 0

        for r in range(len(nums)):
            cur_sum += nums[r]

            while cur_sum >= target:
                min_dis = min(min_dis, r - l + 1)
                cur_sum -= nums[l]
                l += 1
        return min_dis if min_dis != float('inf') else 0