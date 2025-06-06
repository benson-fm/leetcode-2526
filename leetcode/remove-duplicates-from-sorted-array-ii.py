class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # counter
        # while loop since length size is dynamic
        # if it passes the check then increase the index
        # if not
            # pop the element 
            # change the len 
        
        # brute force within constraint
        # count = 0
        # cur_ele = None
        # size = len(nums)
        # idx = 0

        # while idx < size:
        #     if cur_ele == nums[idx]:
        #         if count == 2:
        #             nums.pop(idx)
        #             size -= 1
        #         else:
        #             count += 1
        #             idx += 1
        #     else:
        #         count = 1
        #         cur_ele = nums[idx]
        #         idx += 1

        # return size

        # two pointer approach
        j = 1 # idx 0 will always be part of the arr
        for i in range(1, len(nums)):
            if j == 1 or nums[i] != nums[j - 2]: # with j == 1 we don't need to worry about the j - 2 since it'll automatically say it works 
                nums[j] = nums[i] 
                # the end result will still have the previous stuff it's just the first k elements will be correct 
                j += 1
        return j

        # the confusion i had initially when it came to figuring out
        # the solution came from me just not understading that it wasn't 
        # the index i and looking back at 2 but instead index j