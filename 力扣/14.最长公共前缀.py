#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = str(strs[0])
        for x in strs[1:]:
            xxx = ""
            for y in range(min(len(ans),len(x))):
                if ans[y]!=x[y]:
                    break
                else :
                    xxx+=ans[y]
            ans = xxx
            if ans=="":
                break
        return ans

# @lc code=end

