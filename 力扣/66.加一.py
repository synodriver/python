#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        jin = 1
        for x in range(len(digits)-1, -1, -1):
            if (digits[x] == 9 and jin == 1):
                jin = 1
                digits[x] = 0
            elif (jin == 1):
                digits[x] = digits[x]+1
                jin = 0
            else:
                jin = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
# @lc code=end
