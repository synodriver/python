#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            if target in nums:
                return nums.index(target)
            if nums[-1]<target:
                return len(nums)
            if nums[0]>target:
                return 0
            l= 0
            r = len(nums)-1
            mid = (l+r)//2
            while not (nums[mid]<target<nums[mid+1]):
                if target>nums[mid]:
                    l = mid
                else :
                    r = mid 
                mid = (l+r)//2
            return mid+1
# @lc code=end

