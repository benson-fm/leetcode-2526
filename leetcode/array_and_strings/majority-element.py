class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # brute force
        # iterate through nums and then find the max 
        
        # 0(n) time, O(n) space
        """
        freq = {}
        max_freq = 0
        max_val = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        for val, count in freq.items():
            if count > max_freq:
                max_val = val
                max_freq = count
        
        return max_val
        """

        # O(n log n) time, O(1) space
        """
        nums.sort()
        return nums[len(nums) // 2] 
        """
        # Boyer-Moore Majority Vote O(n) time, O(1) space
        cand = None
        count = 0

        for i in nums:
            if not cand:
                cand = i
                count += 1
            elif cand == i:
                count += 1
            elif cand != i:
                count -= 1
                if count == 0:
                    cand = None

        return cand