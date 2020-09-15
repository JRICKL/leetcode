#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums, target):
        my_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_dict:
                return [my_dict[complement],i]
            else:
                my_dict[nums[i]] = i


# @lc code=end
