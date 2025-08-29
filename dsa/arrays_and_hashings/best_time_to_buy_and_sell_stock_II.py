class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        low = prices[0]
        i = 1
        while i!=len(prices):
            cur_price = prices[i]    
            if cur_price<low:
                low = cur_price
                i += 1
            elif cur_price == low:
                i += 1
                continue
            elif cur_price > low:
                high = cur_price
                while (i+1)!=len(prices) and (prices[i+1]>high):
                    high = prices[i+1]
                    i += 1
                profit += high - low
                low = high
                i += 1
                continue
        return profit
