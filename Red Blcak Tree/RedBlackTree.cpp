
#include <iostream>
#include <queue>

struct TreeNode {
    struct NodeData {
        int value;
        bool color;
        NodeData(int x) : value(x), color(true) {}
    };
    NodeData val;
    TreeNode *left;
    TreeNode *right;
    TreeNode *parent;
    TreeNode(NodeData x) : val(x), left(nullptr), right(nullptr), parent(nullptr) {}
};

class RedBlackTree {
public:
    void insert(TreeNode* node) {
        if (root == nullptr) {
            node->val.color = false;
            root = node;
            return;
        }
        //find the position to insert
        TreeNode *father = find(root, node->val);
        if (node->val.value < father->val.value) {
            father->left = node;
            node->parent = father;
        } else if (node->val.value > father->val.value) {
            father->right = node;
            node->parent = father;
        } else {
            delete node;
            return;
        }
        //deal with violation
        fixInsertViolation(node);
    }

    void remove(int x) {
        TreeNode* node = search(root, x);
        if (node == nullptr) return;
        
        // Node with two children
        if (node->left != nullptr && node->right != nullptr) {
            TreeNode* mini = findMinimum(node->right);
            int miniValue = mini->val.value;
            remove(miniValue);
            node->val.value = miniValue;
            return;
        }
        
        // Node with one child or no child
        TreeNode* son = (node->left != nullptr) ? node->left : node->right;
        TreeNode* father = node->parent;
        
        if (node->val.color == true) {
            // Red node: simply remove
            replaceNode(node, son);
            delete node;
        } else {
            // Black node
            if (son != nullptr && son->val.color == true) {
                // Red child: recolor and remove
                son->val.color = false;
                replaceNode(node, son);
                delete node;
            } else {
                // Black child or no child: need to fix
                if (son == nullptr && father != nullptr) {
                    fixRemoveViolationForNull(father, node);
                }
                replaceNode(node, son);
                delete node;
                if (son != nullptr) {
                    fixRemoveViolation(son);
                }
            }
        }
    }

    TreeNode* getRoot() {
        return root;
    }

    void print(TreeNode* node) {
        std::queue<TreeNode*> q;
        q.push(node);

        while (!q.empty()) {
            TreeNode *newNode = q.front();
            std::cout << "(" << newNode->val.value << ", " << newNode->val.color << ") ";
            q.pop();
            if (newNode->left != nullptr) q.push(newNode->left);
            if (newNode->right != nullptr) q.push(newNode->right);
        }
    }

private:
    TreeNode *root = nullptr;

    // replace node
    void replaceNode(TreeNode* oldNode, TreeNode* newNode) {
        if (oldNode->parent == nullptr) {
            root = newNode;
        } else if (oldNode == oldNode->parent->left) {
            oldNode->parent->left = newNode;
        } else {
            oldNode->parent->right = newNode;
        }
        if (newNode != nullptr) {
            newNode->parent = oldNode->parent;
        }
    }

    //find the position to insert
    TreeNode* find(TreeNode* node, TreeNode::NodeData x) {
        int num = x.value;
        if (num < node->val.value) {
            if (node->left == nullptr) {
                return node;
            } else {
                return find(node->left, x);
            }
        } else if (num > node->val.value) {
            if (node->right == nullptr) {
                return node;
            } else {
                return find(node->right, x);
            }
        } else {
            return node;
        }
    }

    void fixInsertViolation(TreeNode* node) {
        while (node != root && node->parent->val.color == true) {
            TreeNode* father = node->parent;
            TreeNode* grandpa = father->parent;
            
            if (grandpa == nullptr) break;
            
            TreeNode* uncle = (father == grandpa->left) ? grandpa->right : grandpa->left;
            
            if (uncle != nullptr && uncle->val.color == true) {
                // Case 1: Uncle is red - recolor
                grandpa->val.color = true;
                father->val.color = false;
                uncle->val.color = false;
                node = grandpa;
            } else {
                // Case 2: Uncle is black (or null)
                if (father == grandpa->left) {
                    if (node == father->right) {
                        // LR case
                        leftRotate(father);
                        node = father;
                        father = node->parent;
                    }
                    // LL case
                    rightRotate(grandpa);
                } else {
                    if (node == father->left) {
                        // RL case
                        rightRotate(father);
                        node = father;
                        father = node->parent;
                    }
                    // RR case
                    leftRotate(grandpa);
                }
                father->val.color = false;
                grandpa->val.color = true;
                break;
            }
        }
        root->val.color = false;
    }

    void fixRemoveViolation(TreeNode* node) {
        while (node != root && (node == nullptr || node->val.color == false)) {
            TreeNode* father = node->parent;
            if (father == nullptr) break;
            
            if (node == father->left) {
                TreeNode* brother = father->right;
                
                if (brother != nullptr && brother->val.color == true) {
                    // Case 1: Brother is red
                    brother->val.color = false;
                    father->val.color = true;
                    leftRotate(father);
                    brother = father->right;
                }
                
                if (brother == nullptr) break;
                
                if (isBlack(brother->left) && isBlack(brother->right)) {
                    // Case 2: Brother's children are black
                    brother->val.color = true;
                    node = father;
                } else {
                    if (isBlack(brother->right)) {
                        // Case 3: Brother's left child is red
                        if (brother->left != nullptr) {
                            brother->left->val.color = false;
                        }
                        brother->val.color = true;
                        rightRotate(brother);
                        brother = father->right;
                    }
                    // Case 4: Brother's right child is red
                    brother->val.color = father->val.color;
                    father->val.color = false;
                    if (brother->right != nullptr) {
                        brother->right->val.color = false;
                    }
                    leftRotate(father);
                    node = root;
                }
            } else {
                // Symmetric case: node is right child
                TreeNode* brother = father->left;
                
                if (brother != nullptr && brother->val.color == true) {
                    brother->val.color = false;
                    father->val.color = true;
                    rightRotate(father);
                    brother = father->left;
                }
                
                if (brother == nullptr) break;
                
                if (isBlack(brother->left) && isBlack(brother->right)) {
                    brother->val.color = true;
                    node = father;
                } else {
                    if (isBlack(brother->left)) {
                        if (brother->right != nullptr) {
                            brother->right->val.color = false;
                        }
                        brother->val.color = true;
                        leftRotate(brother);
                        brother = father->left;
                    }
                    brother->val.color = father->val.color;
                    father->val.color = false;
                    if (brother->left != nullptr) {
                        brother->left->val.color = false;
                    }
                    rightRotate(father);
                    node = root;
                }
            }
        }
        if (node != nullptr) {
            node->val.color = false;
        }
    }

    void fixRemoveViolationForNull(TreeNode* father, TreeNode* deletedNode) {
        bool isLeftChild = (deletedNode == father->left);
        
        while (father != nullptr) {
            TreeNode* brother = isLeftChild ? father->right : father->left;
            
            if (brother == nullptr) {
                if (father->parent == nullptr) break;
                isLeftChild = (father == father->parent->left);
                father = father->parent;
                continue;
            }
            
            if (brother->val.color == true) {
                brother->val.color = false;
                father->val.color = true;
                if (isLeftChild) {
                    leftRotate(father);
                } else {
                    rightRotate(father);
                }
                brother = isLeftChild ? father->right : father->left;
                if (brother == nullptr) break;
            }
            
            if (isBlack(brother->left) && isBlack(brother->right)) {
                brother->val.color = true;
                if (father->parent == nullptr) break;
                isLeftChild = (father == father->parent->left);
                father = father->parent;
            } else {
                if (isLeftChild) {
                    if (isBlack(brother->right)) {
                        if (brother->left != nullptr) {
                            brother->left->val.color = false;
                        }
                        brother->val.color = true;
                        rightRotate(brother);
                        brother = father->right;
                    }
                    brother->val.color = father->val.color;
                    father->val.color = false;
                    if (brother->right != nullptr) {
                        brother->right->val.color = false;
                    }
                    leftRotate(father);
                } else {
                    if (isBlack(brother->left)) {
                        if (brother->right != nullptr) {
                            brother->right->val.color = false;
                        }
                        brother->val.color = true;
                        leftRotate(brother);
                        brother = father->left;
                    }
                    brother->val.color = father->val.color;
                    father->val.color = false;
                    if (brother->left != nullptr) {
                        brother->left->val.color = false;
                    }
                    rightRotate(father);
                }
                break;
            }
        }
        if (root != nullptr) {
            root->val.color = false;
        }
    }

    void leftRotate(TreeNode* x) {
        TreeNode* y = x->right;
        x->right = y->left;
        if (y->left != nullptr) {
            y->left->parent = x;
        }
        y->parent = x->parent;
        if (x->parent == nullptr) {
            root = y;
        } else if (x == x->parent->left) {
            x->parent->left = y;
        } else {
            x->parent->right = y;
        }
        y->left = x;
        x->parent = y;
    }

    void rightRotate(TreeNode* x) {
        TreeNode* y = x->left;
        x->left = y->right;
        if (y->right != nullptr) {
            y->right->parent = x;
        }
        y->parent = x->parent;
        if (x->parent == nullptr) {
            root = y;
        } else if (x == x->parent->right) {
            x->parent->right = y;
        } else {
            x->parent->left = y;
        }
        y->right = x;
        x->parent = y;
    }

    TreeNode* search(TreeNode* node, int x) {
        if (node == nullptr) return nullptr;
        if (node->val.value == x) return node;
        if (x < node->val.value) {
            return search(node->left, x);
        } else {
            return search(node->right, x);
        }
    }

    TreeNode* findMinimum(TreeNode* node) {
        if (node == nullptr) return nullptr;
        if (node->left == nullptr) return node;
        return findMinimum(node->left);
    }

    bool isBlack(TreeNode* node) {
        return node == nullptr || node->val.color == false;
    }
};

int main() {
    RedBlackTree* tree = new RedBlackTree();
    tree->insert(new TreeNode(10));
    tree->insert(new TreeNode(20));
    tree->insert(new TreeNode(30));
    tree->insert(new TreeNode(15));
    tree->insert(new TreeNode(25));
    tree->insert(new TreeNode(5));
    tree->insert(new TreeNode(1));
    tree->print(tree->getRoot());
    std::cout << std::endl;
    tree->remove(20);
    tree->print(tree->getRoot());
    std::cout << std::endl;
    delete tree;
    return 0;
}