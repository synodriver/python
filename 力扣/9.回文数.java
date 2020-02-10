/*
 * @lc app=leetcode.cn id=9 lang=java
 *
 * [9] 回文数
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        if (x<0){
            return false ;
        }
        int [] a = new int[100];
        int pos= 0;
        while (x!=0){
            a[pos] = x%10;
            x/=10;
            pos++;
        }
        int flag = 0;
        for (int i = 0;i<pos;i++){
            if (a[i]!=a[pos-i-1]){
                flag= 1;
            }
        }
        if (flag==1){
            return false;
        }
        else {
            return true;
        }
    }
}
// @lc code=end

