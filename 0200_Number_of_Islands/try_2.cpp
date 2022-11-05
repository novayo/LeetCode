class Solution {
private:
    int DR[4] = {1,0,-1,0};
    int DC[4] = {0,1,0,-1};
    
    void helper(vector<vector<char>>& grid, int i, int j) {
        int height = grid.size(), width = grid[0].size();
        if (i < 0 || i >= height || j < 0 || j >= width || grid[i][j] != '1') return;
        
        grid[i][j] = '0';
        for (int k=0; k<4; k++) {
            helper(grid, i+DR[k], j+DC[k]);
        }
    }
    
public:
    int numIslands(vector<vector<char>>& grid) {
        int ans = 0;
        int height = grid.size(), width = grid[0].size();
        
        for(size_t i{0}; i<height; i++) {
            for (size_t j{0}; j<width; j++) {
                if (grid[i][j] == '1') {
                    ans++;
                    helper(grid, i, j);
                }
            }
        }
        
        return ans;
    }
};
