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
using umap_int = unordered_map<int, int>;
using umap_vec = unordered_map<int, vector<int>>;

class Solution {
private:
    int dfs(TreeNode* node, int depth, umap_int& height_table, umap_int& depth_table, umap_vec& cousin_table) {
        if (node == nullptr) return -1;
        
        depth_table[node->val] = depth;
        cousin_table[depth].push_back(node->val);
        
        int left = dfs(node->left, depth+1, height_table, depth_table, cousin_table);
        int right = dfs(node->right, depth+1, height_table, depth_table, cousin_table);
        
        height_table[node->val] = max(left, right) + 1;
        return height_table[node->val];
    }
    
public:
    vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
        umap_int height_table;
        umap_int depth_table;
        umap_vec cousin_table;
        height_table[-1] = -1;
        
        dfs(root, 0, height_table, depth_table, cousin_table);
        
        // find top2
        umap_vec top_2_height_table;
        for (auto& [depth, cousin_vec] : cousin_table) {
            int top1 = -1, top2 = -1;
            int top1_h = -1, top2_h = -1;
            
            for (auto& node : cousin_vec) {
                int node_height = height_table[node];
                if (node_height > top1_h) {
                    top2 = top1;
                    top2_h = top1_h;
                    top1 = node;
                    top1_h = node_height;
                }
                else if (node_height > top2_h && node_height <= top1_h) {
                    top2 = node;
                    top2_h = node_height;
                }
            }
            
            top_2_height_table[depth].push_back(top1);
            top_2_height_table[depth].push_back(top2);
        }
        
        // get answer
        vector<int> ans;
        for (auto& node : queries) {
            int depth = depth_table[node];
            int top1 = top_2_height_table[depth][0];
            int top2 = top_2_height_table[depth][1];
            
            if (node == top1) {
                ans.push_back(depth + height_table[top2]);
            } else {
                ans.push_back(depth + height_table[top1]);
            }
        }
        
        return ans;
    }
};
