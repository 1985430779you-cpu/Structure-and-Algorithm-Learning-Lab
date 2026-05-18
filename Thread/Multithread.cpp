#include <chrono>
#include <iostream>
#include <string>
#include <thread>
#include <vector>

#if true

class Test {
public:
    Test() {
        t.push_back(this->test01());
        t.push_back(this->test02());
        t.push_back(this->test03());
        t.push_back(this->test04());
        t.push_back(this->test05());
    }
    std::string test01() {return "test01";}
    std::string test02() {return "test02";}
    std::string test03() {return "test03";}
    std::string test04() {return "test04";}
    std::string test05() {return "test05";}
    std::vector<std::string> getVector() {
        return t;
    }
private:
    std::vector<std::string> t;
};

int main() {
    Test* test = new Test;
    std::thread t([=] () {
        std::vector<std::string> arr = test->getVector();
        int len = arr.size();
        std::cout << "Start processing!" << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        for (int i = 0; i < len; i++) {
            std::cout << arr[i] << std::endl;
            std::this_thread::sleep_for(std::chrono::milliseconds(1000));
        }
    });
    t.join();
    return 0;
}
#endif