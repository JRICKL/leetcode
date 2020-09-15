#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        wordDict = set(wordDict)
        dp = [False for _ in range(length+1)]
        dp[0] = True
        for i in range(length+1):
            for j in range(0,i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break

        return dp[length]
            
# @lc code=end

