#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        l = int(0)
        r = x
        mid = (l+r)//2
        while True:
            if mid**2<=x and (mid+1) **2>=x:
                if mid**2==x:
                    return mid
                elif ((mid+1)**2)==x:
                    return mid+1
                return mid 
            if mid**2>x:
                r = mid
            elif mid**2<x:
                l = mid
            mid = (l+r)//2      
# @lc code=end

