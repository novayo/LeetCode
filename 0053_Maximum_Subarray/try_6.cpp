class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans {INT_MIN}, cur_sum {0};
        
        for (auto& num : nums) {
            cur_sum += num;
            ans = max(ans, cur_sum);
            
            if (cur_sum < 0) {
                cur_sum = 0;
            }
        }
        
        return ans;
    }
};
