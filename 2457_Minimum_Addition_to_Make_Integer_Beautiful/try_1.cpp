class Solution {
public:
    long long makeIntegerBeautiful(long long n, int target) {
        string string_n = to_string(n);
        
        // get total
        int total {0};
        for (auto& ch : string_n) {
            total += ch - '0';
        }
        
        if (total <= target) {
            return 0ll;
        }

        string tmp = "";
        for (int i = string_n.size()-1; i >= 0; i--) {
            char ch = string_n[i];
            if (ch == '0') continue;
            string_n[i] = '0';
            total -= ch - '0';
            
            if (i == 0) {
                tmp = '1' + string_n;
                break;
            }
            
            string_n[i-1] += 1;
            total += 1;
            
            int j = i-1;
            while (j >= 0 && string_n[j] - '0' == 10) {
                string_n[j] = '0';
                if (j > 0) string_n[j-1]++;
                total -= 9;
                j--;
            }
            
            if (j == -1) {
                tmp = '1' + string_n;
                break;
            }
            i = j + 1;
            
            if (total <= target) {
                tmp = string_n;
                break;
            }
        }
        
        if (tmp == "") {
            tmp = '1' + string_n;
        }
        return stoll(tmp) - n;
    }
};
