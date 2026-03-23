class Solution {
public:
    void traverse(TreeNode* root){
        if(root==NULL) return;

        traverse(root->left);
        traverse(root->right);
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp; 
    }
    TreeNode* invertTree(TreeNode* root) {
        traverse(root);
        return root;
        
    }
};
 
