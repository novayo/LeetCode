class Solution {
public:
    string robotWithString(string s) {
        multiset<char> bst;
        for (char ch : s) {
            bst.insert(ch);
        }
        
        string ans = "";
        vector<char> stack;
        for (char ch : s) {
            char smallest = *(bst.begin());
            
            while (stack.size() && stack.back() <= smallest) {
                ans += stack.back();
                stack.pop_back();
            }
            
            if (ch == smallest) {
                ans += ch;
            } else {
                stack.push_back(ch);
            }
            bst.erase(bst.find(ch));
        }
        
        while (stack.size() > 0) {
            ans += stack.back();
            stack.pop_back();
        }
        
        return ans;
    }
};
