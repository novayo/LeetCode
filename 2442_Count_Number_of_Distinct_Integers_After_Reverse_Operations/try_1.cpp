class Solution {
public:
    int countDistinctIntegers(vector<int>& nums) {
        unordered_set<int> set;
        
        for (auto& num : nums) {
            string s_num = to_string(num);
            reverse(s_num.begin(), s_num.end());
            set.insert(stoi(s_num));
            set.insert(num);
        }
        
        return set.size();
    }
};
