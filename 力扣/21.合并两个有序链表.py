#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            N=ListNode(0)
            M=N
            while(l1!=None and  l2!=None):
                if(l1.val<l2.val):
                    N.next=l1
                    l1=l1.next
                else:
                    N.next=l2
                    l2=l2.next
                N=N.next
            if l1!=None:N.next=l1
            else:N.next=l2
            return M.next
# @lc code=end

