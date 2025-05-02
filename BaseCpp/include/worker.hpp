
#pragma once

#include <atomic>
#include <condition_variable>
#include <memory>
#include <thread>

namespace Worker {

class Worker {
public:
  typedef std::shared_ptr<Worker> Ptr;

  Worker() { worker_running_flag_.store(false); }

  virtual ~Worker() {}

  void Start() {
    if (!worker_running_flag_) {
      worker_running_flag_.store(true);
      worker_thread_ = std::thread(&Worker::Run, this);
    }
  }

  void Stop() {
    {
      worker_running_flag_.store(false);
      std::lock_guard<std::mutex> lk(wake_up_mutex_);
      wake_up_cond_.notify_one();
    }

    if (worker_thread_.joinable())
      worker_thread_.join();
  }

  void Interrupt() {
    std::lock_guard<std::mutex> lk(wake_up_mutex_);
    wake_up_cond_.notify_one();
  }

  virtual bool CheckForWakeUp() = 0;

  virtual void EventHandler() = 0;

private:
  void Run() {
    while (worker_running_flag_) {
      {
        std::unique_lock<std::mutex> lk(wake_up_mutex_);
        wake_up_cond_.wait(lk, [this]() {
          return !this->worker_running_flag_ || CheckForWakeUp();
        });
        // TODO maybe double unlock
        /*wake_up_mutex_.unlock();*/
      }

      if (worker_running_flag_) {
        EventHandler();
      } else {
        break;
      }
    }
  }

  std::thread worker_thread_;
  std::mutex wake_up_mutex_;
  std::condition_variable wake_up_cond_;
  std::atomic_bool worker_running_flag_;
};

} // namespace Worker
