class Solution {
public:
    vector<vector<string>> mostPopularCreator(vector<string>& creators, vector<string>& ids, vector<int>& views) {
        int n = creators.size();
        unordered_map<string, int> total_views;
        unordered_map<string, vector<pair<int, string>>> persion_videos;
        
        int highest_view {0};
        for (int i{0}; i < n; i++) {
            string &creator = creators[i], &id = ids[i];
            int &view = views[i];
            total_views[creator] += view;
            persion_videos[creator].push_back({view, id});
            
            if (total_views[creator] > highest_view) highest_view = total_views[creator];
        }
        
        vector<vector<string>> ans;
        for (auto& [creator, view] : total_views) {
            if (view == highest_view) {
                vector<pair<int, string>>& videos = persion_videos[creator];
                sort(videos.begin(), videos.end(), [&](pair<int, string> A, pair<int, string> B) {
                    if (A.first > B.first) return true;
                    else if (A.first < B.first) return false;
                    else return A.second < B.second;                    
                });
                
                ans.push_back(vector<string> {creator, videos[0].second});
            }
        }
        return ans;
    }
};
