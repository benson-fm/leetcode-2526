class Solution:
    def romanToInt(self, s: str) -> int:
        # super long lengthy way 
        # i = 0 
        # val = 0

        # while i < len(s):
        #     if s[i] == 'I':
        #         if i < len(s) - 1:
        #             if s[i + 1] == 'V':
        #                 val += 4
        #                 i += 1
        #             elif s[i + 1] == 'X':
        #                 val += 9
        #                 i += 1
        #             else:
        #                 val += 1
        #         else:
        #             val += 1
        #     elif s[i] == 'V':
        #         val += 5
        #     elif s[i] == 'X':
        #         if i < len(s) - 1:
        #             if s[i + 1] == 'L':
        #                 val += 40
        #                 i += 1
        #             elif s[i + 1] == 'C':
        #                 val += 90
        #                 i += 1
        #             else:
        #                 val += 10
        #         else:
        #             val += 10
        #     elif s[i] == 'L':
        #         val += 50
        #     elif s[i] == 'C':
        #         if i < len(s) - 1:
        #             if s[i + 1] == 'D':
        #                 val += 400
        #                 i += 1
        #             elif s[i + 1] == 'M':
        #                 val += 900
        #                 i += 1
        #             else:
        #                 val += 100
        #         else:
        #             val += 100
        #     elif s[i] == 'D':
        #         val += 500
        #     elif s[i] == 'M':
        #         val += 1000

        #     i += 1

        # return val

        # however this could be achieved with another alternative of using a mapping 
        # the next thing we could do is consider if the value is less than 
        
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0

        for i in range(len(s)):

            # we know this because of a specific pattern
            # notice how in the roman numeral its MCM going from largest to smallest
            # we can use this to our advantage because we know the futher we go the smaller
            # it should get, but if it gets bigger, then we know we could subtract 
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]] # this is what that's doing here 
            else:
                result += roman[s[i]]
        return result