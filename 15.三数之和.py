#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start


class Solution:
    def threeSum(self, nums):
        length = len(nums)-1
        nums = sorted(nums)
        i = -1
        ans_list = []
        while(i < length):
            i = i+1
            if nums[i] > 0:
                break
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            r = length
            l = i+1
            while(l < r):
                my_sum = nums[i] + nums[r]+nums[l]
                if my_sum == 0:
                    ans_list.append([nums[i],nums[l],nums[r]])
                    while(l < r and nums[l] == nums[l+1]):
                        l = l + 1
                    while(l < r and nums[r] == nums[r-1]):
                        r = r - 1
                    l = l + 1
                    r = r - 1
    
                elif my_sum < 0:
                    l = l+1
                elif my_sum > 0:
                    r = r-1
        return ans_list
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,1,2,-1,4,-6]
    ans = s.threeSum(nums)
    print(ans)
