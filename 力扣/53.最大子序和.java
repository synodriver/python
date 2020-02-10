/*
 * @lc app=leetcode.cn id=53 lang=java
 *
 * [53] 最大子序和
 */

// @lc code=start
class Solution {
    public int maxSubArray(int[] nums) {
        // int len = nums.length;
        // for (int i = 1;i<len;i++){
        //     nums[i]=nums[i-1]+nums[i];
        // }
        // int ans= nums[0];
        // for (int i = 1;i<len;i++){
        //     if (ans<nums[i]){
        //         ans = nums[i];
        //     }
        //     for (int j = 0;j<i;j++){
        //         if (ans<nums[i]-nums[j]){
        //             ans = nums[i]-nums[j];
        //         }
        //     }
        // }
        // return ans ;
        int len = nums.length;
        int ans = nums[0];
        int sum = nums[0];
        for (int i = 1;i<len;i++){
            if (sum<0){
                sum=nums[i];
            }
            else {
                sum+=nums[i];
            }
            if (ans<=sum){
                ans = sum;
            }
        }
        return ans ;
    }
}
// @lc code=end

