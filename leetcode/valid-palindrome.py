class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer solution
            # get the alphanums only then do two pointer
            # two pointer and process while you do it 

        # Working solution but it takes time 
        # chgd = ""

        # for l in s:
        #     if l.isalnum():
        #         chgd += l.lower()
        
        # i = 0
        # j = len(chgd) - 1
        # while i < j:
        #     if chgd[i] != chgd[j]:
        #         return False
        #     i += 1
        #     j -= 1

        # return True

        # Optimal Runtime and works
        # O(n) time, O(1) space
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False  
                i += 1
                j -= 1
        return True