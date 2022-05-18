#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        if x>=0:
            x = str(x)
            # print()
            x = x[::-1]    
            for i in range(len(x)):
                if x[i]!='0':
                    return x[i:]
        else:
            x = str(x)
            # print()
            x = f'-{x[::-1][:-1]}'
            # y = x.find('0')
            # print(y)
            # print(x)
            for i in range(1,len(x)):
                # print(x[i])
                if x[i]!='0':
                    return f'-{x[i:]}'
# @lc code=end

