class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # first principles
        # the largest number is at the end use that to your advantage
        # three pointer solution.
        # We compare the last numbers 
            # if nums2 is bigger we put it where r is 
            # if nums1 is bigger we put that there 
        # this makes it a lot easier on our end for adding it there
        # we condinute this process until we've gone through all the
        # elements of n

        # [7, 8, 9, 0, 0, 0]
        # [2, 5, 6]
        # [7, 8, 9, 0, 0, 9]
        # ...
        # [7, 8, 9, 7, 8, 9]
        # At this point we're getting to a point where the midx >= 0
        # is useful 
        # the second part of the conditional states that if its bigger
        # then we add the nums1[midx]
        # the issue is that we've gone through all those 
        # vars
        # midx acts as a we used all the vars here we know 
        # there's nothing smaller
        

        midx = m - 1
        nidx = n - 1
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1
            
            right -= 1