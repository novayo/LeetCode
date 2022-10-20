class Solution {
public:
    int hardestWorker(int n, vector<vector<int>>& logs) {
        int ans_id = logs[0][0], ans_time = logs[0][1];
        int preTime = logs[0][1];
        
        for (int i=1; i < logs.size(); i++) {
            int id = logs[i][0], time = logs[i][1];
            int t = time - preTime;
            if ((ans_time < t) || 
               (ans_time == t && ans_id > id)) {
                ans_time = t;
                ans_id = id;
            }
            preTime = time;
        }
        
        return ans_id;
    }
};

