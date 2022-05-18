#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        ss=[]
        for x in s:
            if(len(ss)==0):
                ss+=x
                continue
            if x==']':
                if (ss[-1]=='['):
                    ss.pop()
                else :
                    ss+=x
            elif x==')':
                if (ss[-1]=='('):
                    ss.pop()
                else :
                    ss+=x
            elif x=='}':
                if (ss[-1]=='{'):
                    ss.pop()
                else :
                    ss+=x
            else :
                ss+=x
        return len(ss) == 0
# @lc code=end

