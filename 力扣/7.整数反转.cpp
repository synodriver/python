/*
 * @lc app=leetcode.cn id=7 lang=cpp
 *
 * [7] 整数反转
 */

// @lc code=start
class Solution
{
public:
    int reverse(int x)
    {
        long long ans = (long long )x;
        long long sum = 0;
        if (x < 0)
        {
            ans = -ans;
        }
        long long  a[40];
        int pos = 0;
        while (ans)
        {
            a[pos++] = (ans % 10);
            ans /= 10;
        }
        for (int i = 0; i <pos; i++)
        {
            sum = sum * 10 + a[i];
            // printf("%lld\n",sum);
        }
        if (sum>INT_MAX){
            return 0;
        }
        if (x < 0)
        {
            return -sum;
        }
        else
        {
            return sum;
        }
    }
};
// @lc code=end

