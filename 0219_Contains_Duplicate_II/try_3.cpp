class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        int n = nums.size();
        
        unordered_set<int> set_window;
        set_window.insert(nums[0]);
        
        int i {0};
        for (int j=1; j<n; j++) {
            if (abs(i-j) > k) {
                set_window.erase(nums[i]);
                i++;
            }
            
            if (set_window.count(nums[j]) > 0) {
                return true;
            }
            
            set_window.insert(nums[j]);
        }
        
        return false;
    }
};
