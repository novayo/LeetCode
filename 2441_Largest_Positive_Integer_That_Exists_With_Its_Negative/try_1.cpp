class Solution {
public:
    int findMaxK(vector<int>& nums) {
        unordered_set<int> set;
        int ans = -1;
        
        for (auto& num : nums) {
            if (set.count(-num) > 0) {
                ans = max(ans, abs(num));
            }
            set.insert(num);
        }
        
        return ans;
    }
};
