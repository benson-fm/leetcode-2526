class Solution:
    def jump(self, nums: List[int]) -> int:
        near = 0
        jump = 0
        far = 0

        while far < len(nums) - 1:
            # farthest represents the furthest index we can reach in the next jump
            # We're checking all paths within our current jump window (near to far)
            # to find the best one that gets us the farthest
            farthest = 0

            for i in range(near, far + 1):
                # From each position in our current window, calculate how far we can jump
                farthest = max(farthest, i + nums[i])

            # Now that we’ve explored this range (near to far),
            # move near to just after far to explore the next level
            near = far + 1

            # Update far to the farthest index we found from this range
            far = farthest

            # We made one jump to reach this new window
            jump += 1

        return jump