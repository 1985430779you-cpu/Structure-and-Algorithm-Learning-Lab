#include <iostream>

class ShallowCopy {
public:
    ShallowCopy(int x) {data = new int(x);}
    ShallowCopy(const ShallowCopy& copy) {data = copy.data;}
    ~ShallowCopy() {
        if (data != nullptr) delete data;
    }
    int* data;
};

class DeepCopy {
public:
    DeepCopy(int x) {data = new int(x);}
    DeepCopy(const DeepCopy& copy) {
        data = new int(*copy.data);
    }
    ~DeepCopy() {
        if (data != nullptr) delete data;
    }
    int* data;
};

int main() {
    ShallowCopy s1(10);
    ShallowCopy s2(s1);
    std::cout << *s1.data << std::endl;
    std::cout << *s2.data << std::endl;
    *s2.data = 20;
    std::cout << *s1.data << std::endl;
    std::cout << *s2.data << std::endl;
    // s1.~ShallowCopy();
    // s2.~ShallowCopy();
    std::cout << "Check" << std::endl; 
    return 0;
}