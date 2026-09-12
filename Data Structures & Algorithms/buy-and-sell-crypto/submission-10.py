class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        



        left = 0
        right = 1
        current_max_profit = 0

        while right <= len(prices)-1:

            if prices[left] >= prices[right]:
                print(prices[left] - prices[right])
                left = right
            
            if prices[left] < prices[right]:
                print(prices[right] - prices[left])
                current_max_profit = max(current_max_profit, prices[right] - prices[left])
            right += 1

        return current_max_profit

