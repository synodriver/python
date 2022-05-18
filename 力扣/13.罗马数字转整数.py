#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        for x in range(len(s)):
            if s[x]=='I':
                if x==len(s)-1:
                    sum+=1
                elif s[x + 1] in ['V', 'X']:
                    sum-=1
                else:
                    sum+=1
            elif s[x]=='X':
                if x==len(s)-1:
                    sum+=10
                elif s[x + 1] in ['L', 'C']:
                    sum-=10
                else:
                    sum+=10
            elif s[x]=='C':
                if x==len(s)-1:
                    sum+=100
                elif s[x + 1] in ['D', 'M']:
                    sum-=100
                else:
                    sum+=100
            elif s[x]=='V':
                sum+=5
            elif s[x]=='L':
                sum+=50
            elif s[x]=='D':
                sum+=500
            elif s[x]=='M':
                sum+=1000
        return sum
            

            
# @lc code=end

