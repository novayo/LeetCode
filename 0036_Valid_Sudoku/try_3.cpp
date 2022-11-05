class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = 9;
        int rows[9][9] {};
        int cols[9][9] {};
        int blocks[9][9] {};
        
        // O(m*n)
        for (int x{0}; x < n; x++) {
            for (int y{0}; y < n; y++) {
                int c = board[x][y] - '1';
                if (c < 0) continue;
                
                int index_blocks = x / 3 * 3 + y / 3;
                if (rows[x][c] || cols[y][c] || blocks[index_blocks][c]) {
                    return false;
                }
                
                rows[x][c] = 1;
                cols[y][c] = 1;
                blocks[index_blocks][c] = 1;
            }
        }
        
        return true;
    }
};
