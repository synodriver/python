#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q= []
        ans = 0
        vis = [0 for _ in range(300)]
        for x in range(len(s)):
            if vis[ord(s[x])]==0:
                vis[ord(s[x])]+=1
                q.append(s[x])
                # print(q)
            else :
                while q[0]!=s[x]:
                    vis[ord(q[0])]-=1
                    q.pop(0)
                vis[ord(q[0])]-=1
                q.pop(0)
                q.append(s[x])
                vis[ord(s[x])]+=1
            ans = max (ans,len(q))
            # print(q)
        return ans 
# @lc code=end

