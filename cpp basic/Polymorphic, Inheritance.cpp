#include <iostream>

using namespace std;

class Data {
public:
    int a = 1;
    int b = 2;
    virtual int plus() {
        return a+b;
    }
};

class calculate : public Data {
public:
    int plus () {
        return a+c;
    }
private:
    int c = 5;
};

class display : public Data {
public:
    int plus () {
        return 10;
    }
};

int main() {
    calculate c1;
    cout << c1.plus() << endl;
    cout << c1.a << endl;
    display d1;
    cout << d1.plus() << endl;
    Data *d2 = new display(); 
    cout << d2->plus() << endl;
}