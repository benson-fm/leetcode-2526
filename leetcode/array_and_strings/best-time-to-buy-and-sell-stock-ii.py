class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # base = 0
        # top = 0
        # profit = 0
        # if len(prices) == 1:
        #     return 0
        
        # while top < len(prices) - 1 and base < len(prices) - 1:
        #     print(top, base, profit)
        #     if prices[base + 1] < prices[base]:
        #         base += 1
        #         top = base + 1
        #     elif prices[top] < prices[top + 1]:
        #         top += 1
        #     else:
        #         profit += prices[top] - prices[base]
        #         base = top
        #         top += 1
        # return profit

        # Working appraoch but goes by window
        # base = 0
        # profit = 0
        # ydy = 0
        # for tdy in range(1, len(prices)):
        #     if prices[ydy] > prices[tdy]:
        #         profit += prices[ydy] - prices[base]
        #         base = tdy
        #     ydy = tdy

        # if prices[ydy] > prices[base]:
        #     profit += prices[ydy] - prices[base]
        # return profit
        
        # Approach to where there's any profit sum
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]: # as long as the one prior is a positive transaction add that difference to the profit 
            # this also eliminates the need to add that last edge case pattern where it goes all the way to the end and isn't calculated
                profit += prices[i] - prices[i - 1]
        return profit