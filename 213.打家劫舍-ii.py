#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 选取第一个或者不选取
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0],nums[1])
        else:
            return max(nums[0] + self.rob1(nums[2:-1]),self.rob1(nums[1:]))


    def rob1(self, nums: List[int]) -> int:
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
# @lc code=end

