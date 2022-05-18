#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        while x < len(nums) - 1:
            while ( x<len(nums)-1 and nums[x]==nums[x+1]):
                nums.pop(x)
            x+=1
        return len(nums)
# @lc code=end

