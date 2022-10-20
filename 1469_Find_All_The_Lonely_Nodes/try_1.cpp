/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    void helper(TreeNode* root, vector<int>& ans) {
        if (!root) return;
        
        helper(root->left, ans);
        helper(root->right, ans);
        
        if ((root->left && !root->right) || (!root->left && root->right)) {
            ans.push_back(root->left ? root->left->val : root->right->val);
        }
        
        return;
    }
    
public:
    vector<int> getLonelyNodes(TreeNode* root) {
        vector<int> ans;
        helper(root, ans);
        return ans;
    }
};
