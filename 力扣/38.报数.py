#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
            def xx(s):
                if len(s)==1:
                    return f'1{s}'
                ss = ""
                sum = 1
                for i in range(len(s)-1):
                    if s[i]==s[i+1]:
                        sum+=1
                    else :
                        ss+=str(sum)
                        ss+=s[i]
                        sum=1
                ss += str(sum) if s[-1]==s[-2] else '1'
                ss+=s[-1]
                return ss
            s= '1'
            di = {}
            di['1']='1'
            for i in range(2,31):
                s = xx(s)
                di[str(i)]=s
            # print(di[str(n)])
            return di[str(n)]
# @lc code=end

