class Solution:
    def trap(self, height: List[int]) -> int:
        # these cars are base case since sides don't count 
        # ptr = 1 

        # amt = 0
        # while ptr < len(height) - 1:
        #     l = ptr - 1
        #     r = ptr + 1
        #     while l >= 0 and r < len(height):
        #         if min(height[l], height[r]) > height[ptr]:
        #             area = (r - l - 1) * min(height[r], height[l])
                    
        #             for i in range(l + 1, r):
        #                 area -= height[i]

        #             amt += area
            
        #             ptr = r
        #             break

        #         if height[l] < height[ptr]:
        #             l -= 1
        #         if height[r] < height[ptr]:
        #             r += 1
        #     else:
        #         ptr += 1
        # return amt

        l = 0 
        r = len(height) - 1
        lMax = height[l]
        rMax = height[r]
        amt = 0
        while l < r:
            if lMax < rMax:
                l += 1
                # if height[l] < lMax:
                #     print("ran")
                #     amt += lMax - height[l]
                # else:
                #     lMax = height[l]
                lMax = max(lMax, height[l])
                amt += lMax - height[l]
            else:
                r -= 1
                # if height[r] < rMax:
                #     amt += rMax - height[r]
                # else:
                #     lMax = height[r]
                rMax = max(rMax, height[r])
                amt += rMax - height[r]
        return amt