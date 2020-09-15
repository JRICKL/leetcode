#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 参考解答：动态规划
        length = len(prices)
        if length < 2:
            return 0
        # 存储数组
        dp = [0]*5
        dp[0] = 0
        dp[1] = -prices[0]
        dp[3] = -float('inf')
        for i in range(length):
            dp[0] = 0
            dp[1] = max(dp[1],-prices[i])
            dp[2] = max(dp[2],dp[1] + prices[i])
            dp[3] = max(dp[3],dp[2] - prices[i])
            dp[4] = max(dp[4],dp[3] + prices[i])

        return max(0,dp[2],dp[4])

# @lc code=end

