#include <chrono>
#include <iostream>
#include <memory>
#include <mutex>
#include <queue>
#include <thread>

#if false
class Test {
public:
    static Test* CreateSingleObject();
    void print();
    ~Test() = default;
private:
    Test() = default;
    Test(const Test& test) = delete;
    Test& operator=(const Test&) = delete;
};

Test* Test::CreateSingleObject() {
    //unique_str帮忙释放内存
    static std::unique_ptr<Test> my_test(new Test());
    //get才能拿到裸指针
    return my_test.get();
}

void Test::print() {
    std::cout << "testing..." << std::endl;
}

int main() {
    Test *test = Test::CreateSingleObject();
    Test *ntr = Test::CreateSingleObject();
    test->print();
    ntr->print();
    std::cout << "test address:" << test << std::endl;
    std::cout << "ntr address:" << ntr << std::endl;
    return 0;
}
#endif

#if true

class Queue {
public:
    static Queue* query(); 
    bool isEmpty() {
        std::lock_guard<std::mutex> locker(m_mutex);
        return q.empty();
    }
    void addTask(int x) {
        std::lock_guard<std::mutex> locker(m_mutex);
        q.push(x);
    }
    bool deleteTask() {
        std::lock_guard<std::mutex> locker(m_mutex);
        if (q.empty()) return false;
        q.pop();
        return true;
    }
    int getTask() {
        std::lock_guard<std::mutex> locker(m_mutex);
        if (q.empty()) return -1;
        return q.front();
    }
    ~Queue() = default;

private:
    Queue() = default;
    Queue(const Queue& queue) = delete;
    Queue& operator=(const Queue&) = delete;
    static std::unique_ptr<Queue> m_task;
    std::queue<int> q;
    std::mutex m_mutex;
};

std::unique_ptr<Queue> Queue::m_task = nullptr;

Queue* Queue::query() {
    if (m_task == nullptr) {
        m_task = std::unique_ptr<Queue>(new Queue());
    }
    return m_task.get();
}

int main() {
    Queue* queue = Queue::query();

    std::thread t1([=] () {
        for (int i = 0; i < 10; i++) {
            queue->addTask(i);
            std::cout << "++push id:" << i
            << " thread:" << std::this_thread::get_id() << std::endl;
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
        }
    });

    std::thread t2([=] () {
        while (!queue->isEmpty()) {
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
            int num = queue->getTask();
            std::cout << "--push id:" << num
            << " thread:" << std::this_thread::get_id() << std::endl;
            queue->deleteTask();
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
        }
    });

    t1.join();
    t2.join();

    return 0;
}
#endif