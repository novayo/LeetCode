class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int n = strs.size();
        int str_len = strs[0].length();
        int ans = 0;
        
        for (int i=0; i < str_len; i++) {
            int cur = 0;
            for (string &str : strs) {
                if (cur > int(str[i])) {
                    ans++;
                    break;
                }
                cur = int(str[i]);
            }
        }
        return ans;
    }
};
