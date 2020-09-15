#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # 用字典方法
        d = {}

        for i in nums:
            if i not in d:
                d[i] = True
            else:
                return True
        return False

        # set 转换为集合判断大小的方法
        # 18/18 cases passed (40 ms)
        # Your runtime beats 93.5 % of python3 submissions
        # Your memory usage beats 16 % of python3 submissions (19 MB)

        if len(set(nums)) == len(nums):
            return False
        else:
            return True
        # list 查询的方式 超时
        # tmp = []
        # for i in nums:
        #     if i not in tmp:
        #         tmp.append(i)
        #     else:
        #         return True
        # return Falsei [chu]
# @lc code=end

