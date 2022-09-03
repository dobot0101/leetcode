class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10001
        # max_price = -1
        profit = 0
        for price in prices:
            # if price < min_price:
            #     min_price = price
            #     max_price = -1
            # elif price > max_price:
            #     max_price = price
            #     profit = max(profit, max_price - min_price)
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
                
        return profit
                
                
                
                
                
            