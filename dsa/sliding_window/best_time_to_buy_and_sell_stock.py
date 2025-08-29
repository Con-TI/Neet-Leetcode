class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
# class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     return max(max([max(prices[i:]) - price for i,price in enumerate(prices)]),0)
            