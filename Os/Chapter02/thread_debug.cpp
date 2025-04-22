/*
 g++ -g -std=c++17 thread_debug.cpp -o dt.out -pthread
 */

#include <chrono>
#include <iostream>
#include <thread>
#include <vector>

class Worker {
public:
  Worker(int id) : id_(id) {}

  void do_work() {
    std::cout << "Thread " << id_ << " started." << std::endl;
    int result = compute(id_);
    std::cout << "Thread " << id_ << " result = " << result << std::endl;
  }

private:
  int id_;

  int compute(int x) {
    std::this_thread::sleep_for(std::chrono::milliseconds(100));
    return x * x;
  }
};

void start_threads(int count) {
  std::vector<std::thread> threads;
  for (int i = 1; i <= count; ++i) {
    Worker w(i);
    threads.emplace_back(&Worker::do_work, w); // 调用成员函数
  }
  for (auto &t : threads) {
    t.join();
  }
}

int main() {
  std::cout << "Main thread started." << std::endl;
  start_threads(3);
  std::cout << "Main thread finished." << std::endl;
  return 0;
}
