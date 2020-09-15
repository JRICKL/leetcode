#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
from collections import deque
class Solution:
    def containsNearbyDuplicate(self, nums:[int], k: int) -> bool:
        # 字典的方法
        d = {}
        for idx,n in enumerate(nums):
            if n not in d:
                d[n]=idx
            else:
                if (idx-d[n])<=k:
                    return True
                else:
                    d[n]=idx
        return False
        
        # 官方解法
        # 利用deque超时
        # d = deque(maxlen=k+1)
        # for i in nums:
        #     d.append(i)
        #     if len(set(d)) != len(d):
        #         return True
        # else:
        #     return False
        


# @lc code=end

