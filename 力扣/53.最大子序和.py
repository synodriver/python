#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = int(nums[0])
        ans = sum
        for x in nums[1:]:
            if (sum<0):
                sum=int(x)
            else :
                sum+=x
            ans = max(ans,sum)
        return ans  
        # a = [0,nums[0]]
        # for x in nums[1:]:
        #     a.append(a[-1]+x)
        # ans = a[1]
        # for i in range(len(a)-1,0,-1):
        #     for j in range(i-1,-1,-1):
        #         ans= max(ans,a[i]-a[j])
        # return ans 

# @lc code=end

