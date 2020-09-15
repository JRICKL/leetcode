#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # min_price = prices[0]
        # for i,price in enumerate(prices[:-1]):
            
        #     if price < min_price:
        #         min_price = price
        #     elif price == min_price:
        #         pass
        #     else:
        #         if prices[i+1]>=price:
        #             pass
        #         else:
        #             profit = profit + price - min_price
        #             min_price = prices[i+1]
        # if prices[-1] > min_price:
        #     profit = profit + prices[-1] - min_price
        
        # return profit
        # 官方解法
        
        length = len(prices)
        profit = 0
        for i in range(1,length):
            if prices[i] > prices[i-1]:
                profit +=prices[i] - prices[i-1]
        return profit
        
# @lc code=end

