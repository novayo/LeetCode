#include<bitset>

using namespace std;

class Solution {
private:
    int helper(int a, int b) {
        // a ^ x = b
        bitset<32> x;
        bitset<32> bit_a(a);
        bitset<32> bit_b(b);

        for (int i=0; i<32; i++) {
            int d1 = bit_a[i], d2 = bit_b[i];
            
            if (d2 == 1) {
                x[i] = d1 == 0 ? 1 : 0;
            } else {
                x[i] = d1;
            }

        }
        return (int) x.to_ulong();
    }
    
public:
    vector<int> findArray(vector<int>& pref) {
        int n = pref.size();
        vector<int> ans;
        ans.push_back(pref[0]);
        
        for (int i=1; i < n; i++) {
            ans.push_back(helper(pref[i-1], pref[i]));
        }
        
        return ans;
    }
};

