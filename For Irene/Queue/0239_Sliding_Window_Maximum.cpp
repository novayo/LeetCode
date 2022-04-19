#include <deque>

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        deque<pair<int,int>> dec_q;
        
        // init
        for (int i=0; i<k; i++){
            while (!dec_q.empty() && dec_q.back().first < nums[i]) {
                dec_q.pop_back();
            }
            
            dec_q.push_back(make_pair(nums[i], i));
        }
        ans.push_back(dec_q.front().first);

        
        // loop
        for (int i=k; i<nums.size(); i++) {
            while (!dec_q.empty() && dec_q.back().first < nums[i]) {
                dec_q.pop_back();
            }
            
            dec_q.push_back(make_pair(nums[i], i));
            
            if (i - dec_q.front().second >= k) {
                dec_q.pop_front();
            }
            
            ans.push_back(dec_q.front().first);
        }
        
        return ans;
    }
};