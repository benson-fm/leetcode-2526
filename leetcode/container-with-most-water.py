class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointer solution 
        # Calculation of area min(height[i], height[j]) * (j - i)
        # maxHold = 0
        # whichever value is most smaller we move 
        
        # Time O(n) Space O(1)
        
        i = 0
        j = len(height) - 1
        maxHold = 0

        while i < j:
            maxHold = max(maxHold, min(height[i], height[j]) * (j - i))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxHold