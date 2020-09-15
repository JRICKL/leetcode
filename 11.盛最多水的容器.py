#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start


class Solution:
    def maxArea(self, height):
        max_value = 0
        j = len(height) - 1
        i = 0
        # use != will serious influence runtime
        while i < j:
            # can omit
            a = j-i
            if height[i]<=height[j]:
                # The formula is as simple as possible. 
                area = a*height[i]
                i = i + 1
            else:
                area = a*height[j]
                j = j- 1
            if area>max_value:
                max_value = area
            # min_height = min(height[i], height[j])
            # area = (j - i)*min_height
            # if area > max_value:
            #     max_value = area
            # if height[i] == min_height:
            #     i = i + 1
            # else:
            #     j = j-1

        return max_value
# @lc code=end
