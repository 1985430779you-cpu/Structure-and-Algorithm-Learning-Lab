/**
 * @file BTree.h / BTree.cpp / main.cpp
 * @brief Implementation of a B-Tree Template Class
 * @details Includes core functionalities such as insert, remove, search and clear.
 * @author WhiteRabbit
 * @date May 17, 2026
 */

#include "BTree.h"

#include <iostream>
#include <vector>

int main() {
    // Test 1: Insertion Logic.
    std::cout << "=== Test 1: Insertion and Node Splitting ===" << std::endl;
    BTree<int> btree(3); // Create a B-Tree of order 3.

    std::vector<int> insert_data = {10, 20, 5, 6, 12, 30, 7};
    
    std::cout << "Inserting elements: ";
    for (auto val : insert_data) {
        std::cout << val << " ";
        btree.insert(val);
    }
    std::cout << std::endl;

    std::cout << "Level-order traversal after insertion:" << std::endl;
    btree.print();

    // Test 2: Search and Existence Check.
    std::cout << "\n=== Test 2: Search Functionality ===" << std::endl;
    std::cout << "Searching for 6: " << (btree.find(6) ? "Found" : "Not Found") << std::endl;
    std::cout << "Searching for 15: " << (btree.find(15) ? "Found" : "Not Found") << std::endl;

    // Test 3: Delete Logic.
    std::cout << "\n=== Test 3: Deletion Operations (Complex Cases) ===" << std::endl;
    
    btree = BTree<int>(3);
    
    std::vector<int> special_data = {20, 10, 30, 25, 15};
    for (auto val : special_data) {
        btree.insert(val);
    }
    
    std::cout << "Structure before deletion:" << std::endl;
    btree.print();

    // Delete element from a leaf node.
    std::cout << "\nDeleting leaf element 25:" << std::endl;
    btree.remove(25);
    btree.print();

    // Delete element from an internal node.
    std::cout << "\nDeleting internal element 20 (Triggers successor replacement):" << std::endl;
    btree.remove(20);
    btree.print();

    // Trigger node merging.
    btree = BTree<int>(3);
    int keys[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    for (int k : keys) btree.insert(k);
    
    std::cout << "\nComplex Merge Test - Before deletion:" << std::endl;
    btree.print();
    
    // Continuous delete to force underflow and merging.
    std::cout << "\nContinuously deleting 1, 2, 3, 4 (Triggers merging logic):" << std::endl;
    btree.remove(1);
    btree.remove(2);
    btree.remove(3);
    btree.remove(4);
    btree.print();

    // Test 4: Clear Tree and Empty Tree Handling.
    std::cout << "\n=== Test 4: Clear Tree and Empty Tree Handling ===" << std::endl;
    btree.clear();
    std::cout << "Is the tree empty after clearing? " << (btree.empty() ? "Yes" : "No") << std::endl;
    
    // Attempt to remove from an empty tree.
    btree.remove(100);
    std::cout << "Attempted to remove element from an empty tree. Program runs normally." << std::endl;

    // Test 5: Duplicate Insertion and Uniqueness.
    std::cout << "\n=== Test 5: Duplicate Insertion and Uniqueness ===" << std::endl;
    btree.insert(100);
    btree.insert(100);
    btree.print();

    std::cout << "\nAll tests completed successfully!" << std::endl;
    return 0;
}