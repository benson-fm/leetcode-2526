class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # We can iterate through each element, then through that
        # We call two sum on the rest of the elements to find that target value
        # nums[i] as a point of caluclation, nums[i + 1:] is two sum to help find the sum of
        # the values to equal 0
        nums.sort()
        combs = set()

        for i in range(len(nums)):    
            j = i + 1
            z = len(nums) - 1
            while j < z:
                if nums[j] + nums[z] + nums[i] == 0:
                    if tuple((nums[i], nums[j], nums[z])) not in combs:
                        combs.add((nums[i], nums[j], nums[z]))
                    j += 1
                elif nums[j] + nums[z] + nums[i] > 0:
                    z -= 1
                else:
                    j += 1
        return [list(comb) for comb in combs]

        # []
        # -1 -1 0