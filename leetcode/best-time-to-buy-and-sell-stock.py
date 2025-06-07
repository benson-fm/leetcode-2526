class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initial pointer approach

        # # 7, 2, 6, 5, 3, 1, 9
        #           ^   ^  ^   ^
        
        # # 1, 2, 3, 4, 5, 6
        #   ^              ^

        # # 7 2 6 1 9 4
        #         ^   ^
        

        profit = 0
        i = 0
        # j = 1

        # while j < len(prices):
        #     profit = max(profit, prices[j] - prices[i])
            
        #     if prices[j] - prices[i] < 0:
        #         i = j

        #     j += 1

        for j in range(1, len(prices)):
            profit = max(profit, prices[j] - prices[i])
            if prices[j] - prices[i] < 0:
                i = j

            
            # elif prices[i] < prices[j]:
            #     j += 1
            # else:
            #     i += 1
            #     if i == j:
            #         j += 1

        return profit


        

        # Time Limit Exceeded
        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         profit = max(profit, prices[j] - prices[i])
        # return profit