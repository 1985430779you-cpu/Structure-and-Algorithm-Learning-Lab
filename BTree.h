#ifndef BTREE_H
#define BTREE_H

#include <functional>
#include <memory>
#include <vector>

template<class T>
class BTreeNode {
public:
    std::vector<T> value;
    std::vector<std::shared_ptr<BTreeNode<T>>> children;
    std::weak_ptr<BTreeNode<T>> parent;
};

template<class T, class Compare = std::less<T>>
class BTree {
public:
    using SharedPtr = std::shared_ptr<BTreeNode<T>>;
    using WeakPtr = std::weak_ptr<BTreeNode<T>>;

    // Constructor: input the order of the BTree.
    BTree(const int& dimension,  const Compare& c = Compare()) : n(dimension), comp(c) {}

    // Delete copy constructor.
    BTree(const BTree&) = delete;

    // Destructor: Release all dynamically allocated memory.
    ~BTree() {
        clear();
        root.reset();
    } 

    // Delete copy assignment operator.
    BTree& operator=(const BTree&) = delete;

    // Default move constructor: Transfer ownership of resources.
    BTree(BTree&&) = default;
        BTree& operator=(BTree&& other) noexcept {
        if (this != &other) {
            clear();            
            root = std::move(other.root);
            comp = std::move(other.comp);
        }
        return *this;
    }

    // Check whether element exists or not.
    bool find(const T& x);

    // Insert element.
    void insert(const T& x);

    // Delete element.
    void remove(const T& x);

    // Check whether the BTree is empty.
    bool empty() const;

    // Check the number of elements in the Btree.
    int size(const SharedPtr& node) const;

    // Clear all the elements in the BTree.
    void clear();

    // Line by line and inorder print.
    void print();
    void inorderPrint(const SharedPtr& node);

    // Return the root of BTree.
    WeakPtr getRoot() {
        return root;
    }


private:
    const int n; // Order of the BTree
    SharedPtr root = nullptr; // Root node
    Compare comp; // Comparator

    bool equal(const T& a, const T& b) const {
        return !comp(a, b) && !comp(b, a);
    }

    bool less(const T& a, const T& b) const {
        return comp(a, b);
    }

    // Find the pos to insert: return BTreeNode and ptr.
    std::pair<SharedPtr, T*> findNodePos(SharedPtr node, const T& x);

    // Fix insert violation.
    void fixInsertViolation(SharedPtr& node);

    // Fix delete violation
    void fixRemoveViolation(SharedPtr& node);

    // Find the minimum value on the right
    std::tuple<SharedPtr, T*> findMinimum(const SharedPtr& node);
};

#endif // BTREE_H