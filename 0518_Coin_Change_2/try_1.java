class Solution {
    public int change(int amount, int[] coins) {
        // dp 為 每個amount的個數
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : coins){
            for (int i=0; i<amount; i++){
                if (i + coin <= amount){
                    dp[i + coin] += dp[i];                   
                }
            }
        }
        return dp[amount];
    }
}
