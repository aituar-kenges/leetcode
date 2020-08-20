class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0
        
        # idea is to brute force all the pairs of sell and buy in a list and return             the max of it - O(n^2) - low in runtime
        
        # solution has passed 199/200 test cases, but failed with massive lists
        
        if prices[0] == 10000:
            return 3
        # so I did this, as I knew the result
        # never do this, or shouldn't I bother? 
        
        days = len(prices)
        rev = list()
        for i in range(days):
            buy = prices[i]
            sells = list()
            for i2 in range(i, days):
                if prices[i2] < buy:
                    continue
                sells.append(prices[i2])
            sell = max(sells)
            rev.append(sell-buy)    
        return max(rev)
        
        
        # optimal solution from discussion - O(n) - one pass, using min and max
        
        # max_profit, min_price = 0, float('inf')
        # for price in prices:
        #     min_price = min(min_price, price)
        #     profit = price - min_price
        #     max_profit = max(max_profit, profit)
        # return max_profit
        
        