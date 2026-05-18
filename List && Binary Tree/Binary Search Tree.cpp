#include <iostream>
#include <functional>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode (int x) : val(x), left(nullptr), right(nullptr) {};
};

class searchTree {
public:
    searchTree (TreeNode *BST) {
        root = BST;
    }

    void insert (int x) {
        function<TreeNode*(TreeNode*)> add;
        add = [&] (TreeNode* root) {
            TreeNode* newnode = new TreeNode(x);
            if (root == nullptr) {return newnode;}
            if (x < root->val) {
                root->left = add(root->left);

            } else if (x > root->val) {
                root->right = add(root->right);               
            } 
            return root;
        };
        root = add(root);
    }

    bool search (int y) {
        function<bool(TreeNode*)> searchValue;
        searchValue = [&] (TreeNode *root) {
            if (root == nullptr) {return false;}
            if (y == root->val) {return true;}
            if (searchValue(root->left) || searchValue(root->right)) {return true;}
            return false;
        };
        return searchValue(root);
    }

    void remove (int z) {
        function<TreeNode*(TreeNode*)> rm;
        rm = [&] (TreeNode* node)->TreeNode* {
            if (node == nullptr) return nullptr;
            if (z < node->val) {
                node->left = rm(node->left);
            } else if (z > node->val) {
                node->right = rm(node->right);
            } else {
                if (node->left == nullptr) {
                    TreeNode* right = node->right;
                    delete node;
                    return right;
                } else if (node->right == nullptr) {
                    TreeNode* left = node->left;
                    delete node;
                    return left;
                } else {
                    TreeNode* left_maxi = findMax(node->left);
                    node->val = left_maxi->val;
                    int tmp = z;
                    z = left_maxi->val;
                    node->left = rm(node->left);
                    z = tmp;
                }
            }
            return node;
        };
        root = rm(root);
    }

    void print () {
        function<void(TreeNode*)> mid;
        mid = [&] (TreeNode *root) {
            if (root == nullptr) {return;}
            mid(root->left);
            cout << root->val << endl;
            mid(root->right);
        };
        mid(root);
    }

    void clear () {
        function<void(TreeNode*)> clearTree;
        // 逐个点删除，不可以只删除根节点
        clearTree = [&] (TreeNode *node) {
            if (node == nullptr) return;
            clearTree(node->left);
            clearTree(node->right);
            delete node;
        };
        clearTree(root);
        root = nullptr; 
    }

private:
    TreeNode *root = nullptr;
    TreeNode *findMax(TreeNode *node) {
        if (node == nullptr) return nullptr;
        while (node && node->right) {
            node = node->right;
        }
        return node;
    }
}; 

int main() {
    TreeNode* root = new TreeNode(50);
    
    root->left = new TreeNode(30);
    root->right = new TreeNode(70);
    
    root->left->left = new TreeNode(20);
    root->left->right = new TreeNode(40);
    root->right->left = new TreeNode(60);
    root->right->right = new TreeNode(80);
    
    root->left->left->left = new TreeNode(10);
    root->left->left->right = new TreeNode(25);
    root->left->right->left = new TreeNode(35);

    searchTree st1(root);
    //st1.print();
    //cout << (st1.search(21) ? "true" : "false") << endl;
    st1.insert(12);
    st1.print();
    st1.remove(40);
    st1.print();
    st1.clear();
    return 0;
}