#include <exception>
#include <iostream>
#include <stack>
#include <stdexcept>

template<class T>
class queue {
public:
    void qpush(T x) {
        s1.push(x);
    }

    void qpop() {
        if (this->qempty()) {
            throw std::invalid_argument("invalid_argument");
        }
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        s2.pop();

    }

    T qfront() {
        if (this->qempty()) {
            throw std::invalid_argument("invalid_argument");
        }
        if (s2.empty()) {
            while (!s1.empty()) {
                s2.push(s1.top());
                s1.pop();
            }
        }
        return s2.top();
    }

    bool qempty() {
        return s1.empty() && s2.empty();
    }

    int qsize() { 
        return s1.size() + s2.size();
    }

private:
    std::stack<T> s1, s2;
};

int main() {
    queue<int> q1;
    try {
        q1.qpush(2);
        q1.qpush(3);
        q1.qpush(4);
        q1.qpop();
        q1.qpop();
        q1.qpop();
        std::cout << q1.qfront() << std::endl;
    } catch(const std::invalid_argument& e) {
        std::cerr << "Error:" << e.what() << std::endl;
    }   
    return 0;
}