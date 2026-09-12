class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        answer_arr = [0]

        for i, num in enumerate(prices):

            for j in range(i+1, len(prices)):
                val = prices[j] - num
                if val < 0:
                    continue
                else:
                    answer_arr.append(val)

        return max(answer_arr)