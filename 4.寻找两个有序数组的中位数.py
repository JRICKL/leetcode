#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            # directly swap rather than use tmp
            nums1,nums2=nums2,nums1
            m,n=n,m
            # tmp = nums1
            # nums1 = nums2
            # nums2 = tmp
            # tmp = m
            # m = n
            # n = tmp
        m_min = 0
        m_max = m
        half_len = int((m+n+1)/2)
        while(m_min <= m_max):
            i = int((m_max + m_min)/2)
            j = half_len - i
            if(i < m_max and (nums2[j-1] > nums1[i])):
                m_min = i + 1
            elif(i >m_min and (nums1[i-1] > nums2[j])):
                m_max = i - 1
            else:
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left= nums1[i-1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])

                if (m+n)%2 == 1:
                    return max_left

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                return (max_left+min_right)/2
# @lc code=end

if __name__ == "__main__":
    nums1 = [3]
    nums2 = [-2,-1]
    s = Solution()
    mid = s.findMedianSortedArrays(nums1,nums2)
    print(mid)