#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        m = prices[0]
        max_profit = 0
        for i in prices:
            if i< m:
                m = i
            profit = i-m
            if profit > max_profit:
                max_profit = profit
        return max_profit
# @lc code=end

