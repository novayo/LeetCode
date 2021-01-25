class Solution {
    public int coinChange(int[] coins, int amount) {
        // dp: amount = 0~amount
        
        int[] dp = new int[amount+1];
        dp[0] = 0;
        for (int _amount = 1; _amount < dp.length; _amount++){
            
            int min = amount+1; // 如果都沒有符合就都不會更新min，則dp會會大於原本的amount
            for (int j = 0; j<coins.length; j++){
                if (coins[j] <= _amount){
                    min = Math.min(min, dp[_amount - coins[j]] + 1);
                }
            }
            dp[_amount] = min;
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}
