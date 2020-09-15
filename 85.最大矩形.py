#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 官方 dp 解法
        # if matrix == []:
        #     return 0
        # m = len(matrix)
        # n = len(matrix[0])
        # dp = [[0 for _ in range(n)] for _ in range(m)]

        # max_area = 0
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == '0':
        #             continue
        #         # if else 第一位处理
        #         width  = dp[i][j] = dp[i][j-1]+1 if j else 1
        #         for k in range(i,-1,-1):
        #             width = min(width,dp[k][j])
        #             max_area = max(max_area,width*(i-k+1))

        # return max_area

        # 改进的dp
        if matrix == []:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        height = [0 for _ in range(n)]
        left = [0 for _ in range(n)]
        right = [n for _ in range(n)]
        max_area = 0
        for i in range(m):
            cur_left,cur_right = 0,n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] +=1
                else:
                    height[j] = 0
            
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j],cur_left)
                else:
                    cur_left = j+1
                    left[j] = 0

            for j in range(n-1,-1,-1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j],cur_right)
                else:
                    cur_right = j
                    right[j]= n

            for j in range(n):
                max_area = max(max_area,height[j]*(right[j] - left[j]))

        return max_area

s = Solution()
s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
# @lc code=end

