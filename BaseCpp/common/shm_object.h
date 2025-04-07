#pragma once

#include <pthread.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#include <string>

namespace apollo::cyber::base {

class ShmObject {
 public:
  ShmObject() = default;
  ShmObject(const std::string& key, size_t size);

  ~ShmObject();

  void* Open(const std::string& key, size_t size);

 private:
  void* OpenOnly();

  std::string key_{0};
  size_t size_{0};

  void* ptr_ = nullptr;
};

template <typename T>
class ShmData {
 public:
  ShmData() = default;
  template <typename... Args>
  ShmData(const std::string& key, Args&&... args) : shm_obj_(key, sizeof(T)) {
    auto* ptr = reinterpret_cast<T*>(shm_obj_.Open(key, sizeof(T)));
    if (ptr == nullptr) {
      return;
    }
    data_ = new (ptr) T(std::forward<Args>(args)...);
  }

  ~ShmData() {
    if (data_ != nullptr) {
      data_->~T();
    }
  }

  T* operator->() { return data_; }
  T& operator*() { return *data_; }

 private:
  ShmObject shm_obj_;
  T* data_ = nullptr;
};

}  // namespace apollo::cyber::base
