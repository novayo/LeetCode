class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        
        vector<vector<int>> ans;
        ans.push_back(intervals[0]);
        for (size_t i=1; i<intervals.size(); i++) {
            int s=intervals[i][0], e=intervals[i][1];
            
            auto& last_ele = ans.back();
            
            if (last_ele[1] < s) {
                ans.push_back(intervals[i]);
            } else {
                last_ele[1] = max(last_ele[1], e);
            }
        }
        
        return ans;
    }
};
