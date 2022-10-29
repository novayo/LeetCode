class Solution {
public:
    bool canPermutePalindrome(string s) {
        unordered_map<char, int> counter;
        
        for (auto& _s : s) {
            counter[_s]++;
        }
        
        int odd = 0;
        for (auto& [k, v] : counter) {
            if (v % 2 == 1) {
                odd++;
            }
        }
        
        return odd <= 1;
    }
};

