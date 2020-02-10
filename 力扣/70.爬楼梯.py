#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def xx(self,n):
        sqrt_5 = 5**0.5
        return int(1/sqrt_5*(((1+sqrt_5)/2)**(n+1)-((1-sqrt_5)/2)**(n+1)))
    def climbStairs(self, n: int) -> int:
        return Solution.xx(self,n)
        
# @lc code=end

