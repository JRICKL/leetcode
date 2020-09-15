#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
import typing
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        length = len(prices)
        if length < 2:
            return 0
        elif k == 0:
            return 0
        # 无限次购买
        # 针对测试用例 1000000000那个
        elif k>(length/2):
            return self.maxP(prices)
        res = 0
        dp = [0]*(2*k+1)
        dp[0] = 0
        dp[1] = -prices[0]
        for i in range(3,2*k,2):
            dp[i] = -float('inf')
        
        for i in range(length):
            dp[0] = 0
            for j in range(1,2*k+1):
                if (j%2) == 1:
                    dp[j] = max(dp[j],dp[j-1]-prices[i])
                else:
                    dp[j] = max(dp[j],dp[j-1]+prices[i])
                    res = max(dp[j],res)
        
        return res

    def maxP(self,prices:List[int])->int:
        length = len(prices)
        profit = 0
        for i in range(1,length):
            if prices[i] > prices[i-1]:
                profit +=prices[i] - prices[i-1]
        return profit
# @lc code=end

