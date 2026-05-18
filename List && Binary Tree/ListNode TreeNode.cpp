#include <cstddef>
#include <iostream>
#include <functional>

using namespace std;

struct TreeNode {
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {};
    int val;
    TreeNode *left;
    TreeNode *right;
};

struct ListNode {
    int val;
    ListNode *next;
    ListNode (int x): val(x), next(nullptr) {};
};

struct doubleListNode {
    int val;
    doubleListNode *prev;
    doubleListNode *next;
    doubleListNode (int x): val(x), prev(nullptr), next(nullptr) {};
};

int main() {
    TreeNode *root = new TreeNode(1);
    TreeNode *node2 = new TreeNode(2);
    TreeNode *node3 = new TreeNode(3);
    TreeNode *node4 = new TreeNode(4);
    TreeNode *node5 = new TreeNode(5);
    TreeNode *node6 = new TreeNode(6);
    root->left = node2;
    root->right = node3;
    node2->left = node4;
    node2->right = node5;
    node3->right = node6;
    
    function<void(TreeNode*)> mid;
    mid = [&] (TreeNode* node) {
        if (node == nullptr) {return;}
        mid(node->left);
        cout << node->val << endl;
        mid(node->right);
    };
    mid(root);

    return 0;
}