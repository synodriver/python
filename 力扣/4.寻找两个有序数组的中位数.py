#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = []
        while (len(nums1)!=0 and len(nums2)!=0):
            # print(nums1[0],nums2[0])
            if nums1[0]<nums2[0]:
                x.append(nums1[0])
                nums1.pop(0)
            elif nums1[0]==nums2[0]:
                x.append(nums1[0])
                x.append(nums2[0])
                nums1.pop(0)
                nums2.pop(0)
            else :
                x.append(nums2[0])
                nums2.pop(0)
        x+=nums1
        x+=nums2
        if len(x)%2==0:
            return (x[len(x)//2-1]+x[len(x)//2])/2.0
        else:
            return x[len(x)//2]

# @lc code=end

