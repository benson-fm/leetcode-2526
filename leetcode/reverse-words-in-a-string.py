class Solution:
    def reverseWords(self, s: str) -> str:
        # with using extra space we could utilize maybe another list then join it with spaces
        # so meaning we would iterate through the list us isalnum() append it to a local var
        # if we get a space then we append to that list and then after that we join it together
        # then use a stack to reverse
        # fmt = []
        # build = ""
        # for l in s:
        #     if not l.isalnum():
        #         if build:
        #             fmt.append(build)
        #         build = ""
        #     else:
        #         build += l
        
        # if build:
        #     fmt.append(build)

        # new = []
        # i = 0
        # lenFmt = len(fmt)
        # while i < lenFmt:
        #     new.append(fmt.pop())
        #     i += 1
        # return ' '.join(new)
        
        # Note that split automatically removes the spaces in betweenadn then we could two pointer
        # O(n) time , O(n) space
        wrds = s.split()
        i = 0
        j = len(wrds) - 1

        while i < j:
            wrds[i], wrds[j] = wrds[j], wrds[i]
            i += 1
            j -= 1
        
        return ' '.join(wrds)

        # For an O(1) solution the start would be to
            # prune the string of the spaces on the outsides or the extra
            # reverse the whole string 
            # reverse those words