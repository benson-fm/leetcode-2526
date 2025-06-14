class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Since we want to find the length of the last word 
        # in a sequence we go ahead and just 
        # take off the spaces to make it better 
        # then once we get the list we can go ahead
        # and return the last element 

        # we could use a for loop to get the last element 
        # that doesn't have a length of 0 


        # super time inefficient solution 
        # li = s.split(' ')
        # i = len(li) - 1

        # while i >= 0:
        #     if len(li[i]) != 0:
        #         return len(li[i])
        #     i -= 1
        
        # the best way to do this is use the function strip
        # which removes trailing white spaces which is the
        # biggest thing you need to consider

        return len(s.strip().split(' ')[-1])