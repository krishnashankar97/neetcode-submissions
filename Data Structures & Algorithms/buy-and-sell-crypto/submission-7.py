class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = float('-inf')
        minBuy = prices[0]

        for s in prices:
            curr_profit = max(curr_profit, s - minBuy)
            minBuy = min(minBuy, s)
        return curr_profit
