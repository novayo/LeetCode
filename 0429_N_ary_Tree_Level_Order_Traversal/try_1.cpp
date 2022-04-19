/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
#include <queue>

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        if (root == nullptr) {
            return vector<vector<int>>();
        }
        
        vector<vector<int>> ans;
        queue<Node*> q;
        
        // init
        q.push(root);
        
        // bfs
        while (!q.empty()){
            queue<Node*> next_q;
            ans.push_back({});
            
            while (!q.empty()){
                Node* node = q.front(); q.pop();
                ans.back().push_back(node->val);
                
                for (auto child : node->children) {
                    next_q.push(child);
                }
            }
            
            q = next_q;
        }
        
        return ans;
    }
};