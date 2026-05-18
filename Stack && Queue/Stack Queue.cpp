#include <iostream>
#include <stdexcept>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode (int x): val(x), next(nullptr) {};
};

class myqueue {
public:
    myqueue() {
        size = 0;
        head = nullptr;
        tail = nullptr;
    }

    void push(int x) {
        ListNode *node = new ListNode(x);
        if (size == 0) {
            head = node;
            tail = node;
        } else {
            tail->next = node;
            tail = node;
        }
        size++;
    }

    void pop() {
        if (size == 0) {throw out_of_range("error");}
        else {
            ListNode *temp = head;
            head = head->next;
            delete temp;
            size--;
            if (head == nullptr) {
                tail = nullptr;
            }
        }
    }

    int front() {
        if (size == 0) {throw out_of_range("error");}
        return head->val;
    }

    int getSize() {
        return size;
    }

    bool empty() {
        return size == 0;
    }

private:
    int size;
    ListNode *head;
    ListNode *tail;
};

class mystack {
public:
    mystack() {
        size = 0;
        head = nullptr;
        tail = nullptr;
    }

    void push(int x) {
        ListNode *node = new ListNode(x);
        if (size == 0) {
            head = node;
            tail = node;
        } else {
            node->next = head;
            head = node;
        }
        size++;
    }

    void pop() {
        if (size == 0) {throw out_of_range("error");}
        else {
            ListNode *temp = head;
            head = head->next;
            delete temp;
            size--;
            if (head == nullptr) {
                tail = nullptr;
            }
        }
    }

    int top() {
        if (size == 0) {throw out_of_range("error");}
        return head->val;
    }

    int getSize() {
        return size;
    }

    bool empty() {
        return size == 0;
    }

private:
    int size;
    ListNode *head;
    ListNode *tail;
};

int main() {
    myqueue st1;
    st1.push(2);
    st1.push(1);
    //st1.pop();
    //st1.pop();
    cout << st1.front() << endl;
    return 0;
}