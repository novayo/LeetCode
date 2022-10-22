class Solution {
private:
    long long helper(vector<int>& nums, int minK, int maxK) {
        int n = nums.size();
        queue<int> min_index;
        queue<int> max_index;
        
        for (int i=0; i<n; i++) {
            if (nums[i] == minK) min_index.push(i);
            if (nums[i] == maxK) max_index.push(i);
        }
        
        long long ans = 0L;
        for (int i=0; i<n; i++) {
            if (min_index.size() == 0 || max_index.size() == 0) {
                break;
            }
            
            int min_i = min_index.front();
            int max_i = max_index.front();
            int valid_i = max(min_i, max_i);
            ans += n - valid_i;
            
            if (min_index.front() == i) {
                min_index.pop();
            }
            if (max_index.front() == i) {
                max_index.pop();
            }
        }
        
        return ans;
    }
    
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        int n = nums.size();
        long long ans = 0L;
        
        for (int i=0; i<n; i++) {
            if (!(minK <= nums[i] && nums[i] <= maxK)) continue;
            
            int j = i;
            while (j<n && minK <= nums[j] && nums[j] <= maxK) j++;
            
            vector<int> slice_nums (nums.begin()+i, nums.begin()+j);
            ans += helper(slice_nums, minK, maxK);
            i = j;
        }
        
        return ans;
    }
};
