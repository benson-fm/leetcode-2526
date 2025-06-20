class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # we convert s to a stack
        # then from there we start at the end of t for our traversal and go down
        # we pop based on the letter at the top
        # once len(s) < 0 return true
        # else return false

        # Time complexity: O(len(s) + len(t)) space: O(len(s)) 
        # stck = list(s)
        # i = len(t) - 1
        # while i >= 0 and len(stck) > 0:
        #     top = stck[-1]
        #     if t[i] == top:
        #         stck.pop()
        #     i -= 1
        # return len(stck) == 0

        # Two pointer solution
        # Time O(t), Space O(1)
        sptr = 0
        for i in range(len(t)):
            if sptr >= len(s):
                break

            val = s[sptr]
            if t[i] == val:
                sptr += 1
        return sptr == len(s)