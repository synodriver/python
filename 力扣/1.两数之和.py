#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            for x in nums:
                if (target-x) in nums :
                    if target-x ==x:
                        if x in nums[nums.index(x)+1:]:
                            return nums.index(x),nums[nums.index(x)+1:].index(x)+nums.index(x)+1
                    else :
                        return nums.index(x),nums.index(target-x)
# @lc code=end

