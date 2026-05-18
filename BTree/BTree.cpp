#include "BTree.h"

#include <algorithm>
#include <iostream>
#include <memory>
#include <functional>
#include <queue>

// Check whether element exists or not.
template<class T, class Compare>
bool BTree<T, Compare>::find(const T& x) {
    auto [node, index] = findNodePos(root, x);
    if (node == nullptr || index == -1) return false;
    if (index < node->value.size() && equal(x, node->value[index])) {
        return true;
    }
    return false;
}

// Insert element.
template<typename T, typename Compare>
void BTree<T, Compare>::insert(const T& x) {
    // if root is empty, update root
    if (root == nullptr) {
    root = std::make_shared<BTreeNode<T>>();
    root->value.push_back(x);
    return;
    }
    auto [node, index] = findNodePos(root, x);
    // if x exists, return
    if (index != -1 && index < node->value.size() && equal(x, node->value[index])) return;
    typename std::vector<T>::iterator it;
    if (index == -1) {
        it = node->value.end();
    } else {
        it = node->value.begin() + index; 
    }
    node->value.insert(it, x);
    fixInsertViolation(node);
}

// Delete element.
template<typename T, typename Compare>
void BTree<T, Compare>::remove(const T& x) {
    if (root == nullptr) return;
    auto [node, index] = findNodePos(root, x);
    if (index == -1 || !equal(x, node->value[index])) return;
    if (!node->children.empty()) {
        int child_i = index + 1;
        auto [min_node, min_index] = findMinimum(node->children[child_i]);
        T val = min_node->value[min_index];
        remove(val);
        auto [new_node, new_index] = findNodePos(root, x);
        if (new_index >= 0 && new_index < new_node->value.size()) {
            new_node->value[new_index] = val;
        }
    } else {
        node->value.erase(node->value.begin() + index);
        fixRemoveViolation(node);
    }
}

// Check whether the BTree is empty.
template<typename T, typename Compare>
bool BTree<T, Compare>::empty() const {
    return root == nullptr;
}

// Check the number of elements in the Btree.
template<typename T, typename Compare>
int BTree<T, Compare>::size(const SharedPtr<T>& node) const {
    if (node == nullptr) return 0;
    int cnt = node->value.size();
    for (auto child : node->children) {
        cnt += size(child);
    }
    return cnt;
}

// Clear all the elements in the BTree.
template<typename T, typename Compare>
void BTree<T, Compare>::clear() {
    if (root == nullptr) return;
    
    std::vector<SharedPtr<T>> stack = {root};
    
    while (!stack.empty()) {
        SharedPtr<T> node = stack.back();
        stack.pop_back();
        
        for (auto& child : node->children) {
            stack.push_back(child);
        }
        
        node->children.clear();
        node->value.clear();
    }
    
    root.reset();
}

// Print line by line.
template<typename T, typename Compare>
void BTree<T, Compare>::print() {
    if (this->root == nullptr) return;
    std::queue<SharedPtr<T>> q{};
    q.push(this->root);
    std::queue<SharedPtr<T>> tmp{};
    while (!q.empty()) {
        tmp.swap(q);
        while (!tmp.empty()) {
            SharedPtr<T> node = tmp.front();
            tmp.pop();
            for (auto child : node->children) {
                q.push(child);
            }
            for (auto val : node->value) {
                std::cout << val << " ";
            }
            std::cout << "|" << " ";
        }
        std::cout << std::endl;
    }
}

//Inorder print: Child[0] -> value[0] -> Child[1] -> value[1]...
template<typename T, typename Compare>
void BTree<T, Compare>::inorderPrint(const SharedPtr<T>& node) {
    if (node == nullptr) return;
    for (int i = 0; i < node->value.size(); i++) {
        if (i < node->children.size()) {
            inorderPrint(node->children[i]);
        }
        std::cout << node->value[i] << " ";
    }
    
    if (!node->children.empty()) {
        inorderPrint(node->children.back());
    }
}

// Find the pos to insert: return BTreeNode and ptr.
template<typename T, typename Compare>
std::pair<SharedPtr<T>, int> BTree<T, Compare>::findNodePos(SharedPtr<T> node, const T& x) {
    if (node == nullptr) return {nullptr, -1};
    if (node->value.empty()) return {node, 0};
    for (int i = 0; i < node->value.size(); i++) {
        if (equal(x, node->value[i])) return {node, i};
        else if (less(x, node->value[i])) {
            // if its children is not empty, then go on
            // else insert this value at current node
            if (!node->children.empty()) {
                return findNodePos(node->children[i], x);
            }
            return {node, i};
        }
    }
    // if this value is larger than all the elements at current node
    if (!node->children.empty()) {
        // if it is not leaf node, then go on
        return findNodePos(node->children.back(), x);
    }
    // if it is leaf node, insert at the vector end
    return {node, -1};
}

// Fix insert violation.
template<typename T, typename Compare>
void BTree<T, Compare>::fixInsertViolation(SharedPtr<T>& node) {
    int size = node->value.size();
    if (size < this->n) return;
    auto it = node->value.begin() + size / 2;
    SharedPtr<T> left = std::make_shared<BTreeNode<T>>();
    left->value.assign(node->value.begin(), it);
    SharedPtr<T> right = std::make_shared<BTreeNode<T>>();
    right->value.assign(it + 1, node->value.end());
    left->value.reserve(n);
    right->value.reserve(n);

    // have children
    if (!node->children.empty()) {
        auto child_mid = node->children.begin() + (size / 2 + 1);
        left->children.assign(node->children.begin(), child_mid);
        right->children.assign(child_mid, node->children.end());
        for (auto child : left->children) {
            if (child) child->parent = left;
        }
        for (auto child : right->children) {
            if (child) child->parent = right;
        }
    }

    SharedPtr<T> father = nullptr;
    // don't have parent
    if (node->parent.lock() == nullptr) {
        father = std::make_shared<BTreeNode<T>>();
        father->value.push_back(*it);
        left->parent = father;
        father->children.push_back(left);
        right->parent = father;
        father->children.push_back(right);
        this->root = father; 
    // have parent
    } else {
        father = node->parent.lock();
        auto child_it = std::find(father->children.begin(), father->children.end(), node);
        int i = child_it - father->children.begin();
        father->children[i] = left;
        left->parent = father;
        father->children.insert(father->children.begin() + i + 1, right);
        right->parent = father;
        father->value.insert(father->value.begin()+i, *it);
    }
    node.reset();
    // check parent
    if (father != nullptr) {
        fixInsertViolation(father);
    }
}

// Fix delete violation
template<typename T, typename Compare>
void BTree<T, Compare>::fixRemoveViolation(SharedPtr<T>& node) {
    int tolerance = (this->n + 1) / 2 - 1;
    if (node->value.size() >= tolerance) return;
    // don't have father
    SharedPtr<T> father = node->parent.lock();
    if (father == nullptr && node->value.size() > 0) return;
    if (father == nullptr) {
        if (!node->children.empty()) {
            this->root = node->children[0];
            this->root->parent.reset();                
        } else {
            this->root = nullptr;
        }
        node.reset();
        return;
    }

    int i = std::find(father->children.begin(), father->children.end(), node) - father->children.begin();
    SharedPtr<T> left = (i-1) >= 0 ? father->children[i-1] : nullptr;
    SharedPtr<T> right = (i+1) < father->children.size() ? father->children[i+1] : nullptr;
    if (left != nullptr && left->value.size() > tolerance) {
        node->value.insert(node->value.begin(), father->value[i-1]);
        father->value[i-1] = left->value.back();
        left->value.pop_back();
        if (!node->children.empty()) {
            node->children.insert(node->children.begin(),left->children.back());
            node->children.front()->parent = node;
            left->children.pop_back();
        }
    } else if (right != nullptr && right->value.size() > tolerance) {
        node->value.push_back(father->value[i]);
        father->value[i] = right->value.front();
        right->value.erase(right->value.begin());
        if (!node->children.empty()) {
            node->children.push_back(right->children.front());
            node->children.back()->parent = node;
            right->children.erase(right->children.begin());
        }            
    } else {
        if (left != nullptr) {
            left->value.push_back(father->value[i-1]);
            left->value.insert(left->value.end(), node->value.begin(), node->value.end());
            if (!node->children.empty()) {
                for (auto child : node->children) child->parent = left;
                left->children.insert(left->children.end(), node->children.begin(), node->children.end());
            } 
            father->value.erase(father->value.begin()+i-1);
            father->children.erase(father->children.begin() + i);
        } else if (right != nullptr) {
            right->value.insert(right->value.begin(),father->value[i]);
            right->value.insert(right->value.begin(), node->value.begin(), node->value.end());
            if (!node->children.empty()) {
                for (auto child : node->children) child->parent = right;
                right->children.insert(right->children.begin(), node->children.begin(), node->children.end());
            }                 
            father->value.erase(father->value.begin()+i);
            father->children.erase(father->children.begin() + i);
        }
        node.reset();
        fixRemoveViolation(father);
    }
}

// Find the minimum value on the right
template<typename T, typename Compare>
std::pair<SharedPtr<T>, int> BTree<T, Compare>::findMinimum(const SharedPtr<T>& node) {
    SharedPtr<T> son = node;
    while (!son->children.empty()) {
        son = son->children[0];
    }
    return {son, 0};
}

template class BTree<int>;
template class BTree<short>;
template class BTree<long>;
template class BTree<long long>;
template class BTree<unsigned int>;
template class BTree<float>;
template class BTree<double>;
template class BTree<long double>;
template class BTree<char>;
template class BTree<std::string>;
template class BTree<int*>; 
template class BTree<int, std::greater<int>>;
template class BTree<double, std::greater<double>>;
template class BTree<std::string, std::greater<std::string>>;