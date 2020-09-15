#
# @lc app=leetcode.cn id=375 lang=python3
#
# [375] 猜数字大小 II
#

# @lc code=start
import typing
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp = [[0]*(n+1)]*(n+1)
        dp = [[0 for _  in range(n+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            dp[i][i] = 0
        for i in range(1,n):
            dp[i][i+1]=i
        # length 为1 和 2 的已经初始化了
        if n <3:
            return dp[1][n]
        for length in range(3,n+1):
            for start in range(1,n-length+2):
                minres = float('inf')
                for p in range(start+1,start+length-1):
                    res = p + max(dp[start][p-1],dp[p+1][start+length-1])
                    minres = min(res,minres)

                dp[start][start+length -1] = minres
        
        return dp[1][n]

s = Solution()
print(s.getMoneyAmount(4))
# @lc code=end

