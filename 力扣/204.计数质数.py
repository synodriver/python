#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        vis = []
        for x in range(n+1):
            vis.append(0)
        for i in range(2,n+1):
            if vis[i]==0:
                for j in range(i+i,n+1,i):
                    vis[j]=1
        sum = 0
        for i in range(2,n):
            if vis[i]==0:
                sum+=1
        return sum
# @lc code=end

