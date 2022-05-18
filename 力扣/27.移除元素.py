#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        while x < len(nums):
            if nums[x]==val:
                nums.pop(x)
            else :
                x+=1
        return len(nums)
# @lc code=end

