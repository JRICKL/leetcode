#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 错误，可以跳过多间房，而且没有使用动态规划
        # return max(sum([x for x in nums[::2]]),sum([x for x in nums[1::2]]))

        length = len(nums)
        if length ==0:
            return 0
        if length == 1:
            return nums[0]
        dp = [0 for _ in range(length)]
        dp[0]= nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,length):
            dp[i] = max(dp[i-2] + nums[i],dp[i-1])
        return dp[length-1]

s = Solution()
s.rob([1,2,3,1])
# @lc code=end

