class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # Solution with recursion that missed a few test cases
        # def rec(idx, nums):
        #     # if idx == len(nums) - 1:
        #     #     return True
        #     # elif idx >= len(nums):
        #     #     return False
        #     # else:
        #     for i in range(nums[idx] + 1):
        #         if i + idx == len(nums) - 1:
        #             return True
        #         elif i + idx < len(nums) and i != 0:
        #             return rec(i + idx, nums)
        #     return False

        # Solution 
        # gas = nums[0]
        # n = 0
        # for num in nums:
        #     if n >= len(nums) - 1:
        #         return True
        #     if gas == 0:
        #         if num != 0:
        #             gas = num
        #         else:
        #             return False
        #     if num > gas:
        #         gas = num
        #     gas -= 1
        #     n += 1
        # return True

        # Optimized Solution
        # Instead of calculating every possibility we could
        # just think about it as a trip to see how far we 
        # could go, regardless we're trying to land at the dot
        gas = 0 # how many spaces left to move
        for n in nums: # iteratre trhough the list
            if gas < 0: # if we end up not having enough from the ast we return false
                return False
            elif n > gas: # this is the one that mostly runs where if we're able to get more gass than what we currenlty have then this becomes what we get 
                gas = n
            gas -= 1 # after every moment minus 1 
        return True # if we get through regardless if we pass through of on the dot then we know there is some possible iteration for us to get to that point
        """
        gas = 2
        2 3 1 1 4
        ^
        gas = 3
        2 3 1 1 4
          ^
        
        gas = 2, 1, 4
        2 3 1 1 4
            ^ ^ ^ 
        
        Note it's not on getting exact to the dot 
        We just need to get to this point
        """