#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lenn = len(nums1)
        num = 0
        while nums2:
            if nums2[0]<=nums1[num] or nums1[num]==0:
                nums1.insert(num,nums2[0])
                nums2.pop(0)
                if not nums2:
                    break
            else:
                num+=1
        
# @lc code=end

