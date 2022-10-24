class Solution {
private:
    int ans=0;
    
    void helper(vector<bitset<26>>& arr, int idx, bitset<26> cur_val) {
        if (idx >= arr.size()) {
            if (cur_val.count() > ans) {
                ans = cur_val.count();
            }
            return;
        }
        
        // not choose
        helper(arr, idx+1, cur_val);
        
        // choose
        if ((cur_val & arr[idx]).count() == 0) {
            helper(arr, idx+1, cur_val | arr[idx]);
        }
    }
    
public:
    int maxLength(vector<string>& arr) {
        // covert into bit
        vector<bitset<26>> map;
        for (auto& string : arr) {
            bool valid = true;
            bitset<26> bit;
            for (char& s : string) {
                if (bit[s - 'a'] == 1) {
                    valid = false;
                    break;
                }
                bit[s - 'a'] = 1;
            }
            if (valid) map.push_back(bit);
        }
        
        // knapsack
        helper(map, 0, bitset<26>{});
        
        return ans;
    }
};

