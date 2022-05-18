#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s.split(' ')
        return next((len(s[i]) for i in range(len(s)-1,-1,-1) if s[i]!=''), 0)
# @lc code=end

