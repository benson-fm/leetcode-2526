class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = "" # common string to be returned
        smallest = min(strs) # smallest string that can be compared
        for i in range(len(smallest)): # loops through smallest string
            letter = smallest[i] # gets the letter we're looking at
            stop = False # gets the stop function for false
            for word in strs: # moves onto comparing each word
                if word[i] != letter: # checks the letter if its not true
                    stop = True # with the stop it makes it true
                    break # breaks
            if stop: # if we stopped because the letters don't match
                break # we get out 
            common += word[i] # if everything passed add the letter
        return common  # return the common