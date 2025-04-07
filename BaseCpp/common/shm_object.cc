#include "shm_object.h"

#include <errno.h>
#include <fcntl.h>

#include <string>
#include <iostream>

#ifndef AERROR
#define AERROR std::cout
#define ADEBUG std::cout
#endif

namespace apollo::cyber::base {

ShmObject::ShmObject(const std::string& key, size_t size) : key_(key), size_(size) {
  Open(key, size);
}

ShmObject::~ShmObject() {}

void* ShmObject::OpenOnly() {
  // get managed_shm_
  int fd = shm_open(key_.c_str(), O_RDWR, 0644);
  if (fd == -1) {
    AERROR << "get shm failed: " << (errno);
    return nullptr;
  }

  struct stat file_attr;
  if (fstat(fd, &file_attr) < 0) {
    AERROR << "fstat failed: " << (errno);
    close(fd);
    return nullptr;
  }

  // attach managed_shm_
  ptr_ = mmap(nullptr, file_attr.st_size, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
  if (ptr_ == MAP_FAILED) {
    AERROR << "attach shm failed: " << (errno);
    close(fd);
    return nullptr;
  }

  close(fd);
  return ptr_;
}

void* ShmObject::Open(const std::string& key, size_t size) {
  key_ = key;
  size_ = size;
  int fd = shm_open(key_.c_str(), O_RDWR | O_CREAT | O_EXCL, 0644);
  if (fd < 0) {
    if (EEXIST == errno) {
      ADEBUG << "shm already exist, open only.";
      return OpenOnly();
    } else {
      AERROR << "create shm failed, error: " << (errno);
      return nullptr;
    }
  }

  if (ftruncate(fd, size_) < 0) {
    AERROR << "ftruncate failed: " << (errno);
    close(fd);
    return nullptr;
  }

  ptr_ = mmap(nullptr, size_, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
  if (ptr_ == MAP_FAILED) {
    AERROR << "attach shm failed:" << (errno);
    close(fd);
    shm_unlink(key_.c_str());
    return nullptr;
  }

  close(fd);
  return ptr_;
}

}  // namespace apollo::cyber::base
