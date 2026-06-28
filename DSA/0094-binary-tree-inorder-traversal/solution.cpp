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
public:
    vector<int> inorderTraversalHelper(TreeNode* root, vector<int>& traverse) {
        if (root == nullptr) {
            return {};
        }
        if (root->left != nullptr) {
            inorderTraversalHelper(root->left, traverse);
        }
        traverse.push_back(root->val);
        if (root->right != nullptr) {
            inorderTraversalHelper(root->right, traverse);
        }

        return traverse;
    }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> traverse;

        return inorderTraversalHelper(root, traverse);
    }
};


/* class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        vector<int>traverse = {};
        if (root->left != nullptr) {
            traverse.insert(traverse.end(), inorderTraversal(root->left).begin(), inorderTraversal(root->left).end());
        }
        traverse.push_back(root->val);
        if (root->right != nullptr) {
            traverse.insert(traverse.end(), inorderTraversal(root->right).begin(), inorderTraversal(root->right).end());
        }
        return traverse;
        
    }
}; */
