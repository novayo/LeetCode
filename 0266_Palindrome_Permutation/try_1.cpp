class Solution {
public:
    bool canPermutePalindrome(string s) {
        int counter[26] {};

        for (auto& _s : s) {
            counter[_s - 'a']++;
        }

        int odd = 0;
        for (int& v : counter) {
            if (v % 2 == 1) {
                odd++;
            }
        }

        return odd <= 1;
    }
};
