class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Brute force
        # iterate through and get the counts of r the values 
        # then from there iterate through that dict and return all the 
        # instances where it's greater than int(n / 3 )
        
        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1
        # return [ key for key, val in counts.items() if val > int(len(nums) / 3) ]

        # two vars 
        # O(n), O(1)
        cnt1, cnt2 = 0, 0
        maj1, maj2 = 0, 0

        # The initial struggle was the sort of counting parts when it comes to looking at this
        # How this works is that it collects the the two most maximum values 
        # We can think about it as oh if this value doesn't fit to that one and the other
        # one is empty then we can just set that as the value there since we know the prev 
        # value isn't a maximum

        # [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        # First 1 is set as the maj1 , 2
        # Then 2 is set as the maj2 , 3
        # we then move on with to 3
            # since it doesn't match all values we 
            # just decrease everything down
            # It's like a total, contribution since this impacts
            # the overall amount these maxes have over 
            # the others,  
            # THE "CANCELATION EFFECT"
        # even tuall it becomes
        # maj1 , 3, cnt 1
        # maj2, 2, cnt 1

        # then we get to 4 which 
        # decreases both by 1 
        # then end up with maj1, 4, cnt, 2
        # maj2 is just 2 with 2 

        # We then perform a check to ensure that the count
        # is higher than the others, and then it returns nothing

        # We have to think about what's maximum ocurrences, and in this case it's 2
        for num in nums:
            if num == maj1:
                cnt1 += 1
            elif num == maj2:
                cnt2 += 1
            elif cnt1 == 0:
                maj1 = num
                cnt1 += 1
            elif cnt2 == 0:
                maj2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        c1 = 0
        c2 = 0
        
        for num in nums:
            if num == maj1:
                c1 += 1
            
            if num == maj2:
                c2 += 1
        
        res = []
        
        if c1 > len(nums) // 3:
            res.append(maj1)
        
        if c2 > len(nums) // 3 and maj2 not in res:
            res.append(maj2)
        return res