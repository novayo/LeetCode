class Solution {
public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        
        int MOD = k;
        int M = 1e9 + 7;
        
        vector<vector<unordered_map<int, int>>> dp(m, vector<unordered_map<int, int>>(n, unordered_map<int, int>{}));
        
        dp[0][0][grid[0][0] % MOD] = 1;
        for (int i=1; i<m; i++) {
            int val = grid[i][0];
            for (auto &[k, v] : dp[i-1][0]) {
                dp[i][0][(k+val) % MOD] += v % M;
            }
        }
        
        for (int j=1; j<n; j++) {
            int val = grid[0][j];
            for (auto &[k, v] : dp[0][j-1]) {
                dp[0][j][(k+val) % MOD] += v % M;
            }
        }
        
        for (int i=1; i<m; i++) {
            for (int j=1; j<n; j++) {
                int val = grid[i][j];
                
                for (auto &[k, v] : dp[i-1][j]) {
                    dp[i][j][(k+val) % MOD] += v % M;
                }
                
                for (auto &[k, v] : dp[i][j-1]) {
                    dp[i][j][(k+val) % MOD] += v % M;
                }
            }
        }
        
        return dp[m-1][n-1][0] % M;
    }
};
