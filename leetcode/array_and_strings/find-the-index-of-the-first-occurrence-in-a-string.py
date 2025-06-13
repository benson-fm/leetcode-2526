class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

        # You need to add the +1 to account that the length 
        # can be asked plus one to include the last element

        # "abc", "c"
        # range(3 - 1 + 1)
        # last i would be 3 
        # haystack[0:1]
        # haystack[1:2]
        # haystack[2:3]

        # "missisippi", "pi"
        # range(10 - 2 + 1)
        # last i would be 9 
        # haystack[0:1]
        # haystack[1:2]
        # haystack[2:3]