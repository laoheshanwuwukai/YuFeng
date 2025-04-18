
#include <cstring>
#include <dirent.h>
#include <fstream>
#include <grp.h>
#include <iostream>
#include <limits.h>
#include <pwd.h>
#include <sstream>
#include <string>
#include <sys/resource.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <vector>

void print_basic_info() {
  pid_t pid = getpid();
  pid_t ppid = getppid();
  uid_t uid = getuid();
  gid_t gid = getgid();
  char exe_path[PATH_MAX];
  ssize_t len = readlink("/proc/self/exe", exe_path, sizeof(exe_path) - 1);
  if (len != -1)
    exe_path[len] = '\0';

  struct passwd *pw = getpwuid(uid);
  struct group *gr = getgrgid(gid);

  std::cout << "=== Basic Process Info ===\n";
  std::cout << "PID: " << pid << "\n";
  std::cout << "PPID: " << ppid << "\n";
  std::cout << "UID: " << uid << " (" << (pw ? pw->pw_name : "unknown")
            << ")\n";
  std::cout << "GID: " << gid << " (" << (gr ? gr->gr_name : "unknown")
            << ")\n";
  std::cout << "Executable: " << exe_path << "\n";
}

void print_memory_info() {
  std::ifstream status("/proc/self/status");
  std::string line;

  std::cout << "\n=== Memory Info (/proc/self/status) ===\n";
  while (std::getline(status, line)) {
    if (line.find("Vm") == 0) {
      std::cout << line << "\n";
    }
  }
}

void print_cpu_info() {
  std::ifstream stat("/proc/self/stat");
  std::string val;
  std::vector<std::string> fields;
  while (stat >> val)
    fields.push_back(val);

  std::cout << "\n=== CPU Info (/proc/self/stat) ===\n";
  if (fields.size() > 17) {
    long utime = std::stol(fields[13]);
    long stime = std::stol(fields[14]);
    long nice = std::stol(fields[18]);
    std::cout << "User CPU time (clock ticks): " << utime << "\n";
    std::cout << "System CPU time (clock ticks): " << stime << "\n";
    std::cout << "Nice value: " << nice << "\n";
  }
}

void print_limits_info() {
  std::ifstream limits("/proc/self/limits");
  std::string line;

  std::cout << "\n=== Resource Limits (/proc/self/limits) ===\n";
  while (std::getline(limits, line)) {
    std::cout << line << "\n";
  }
}

void print_cwd() {
  char cwd[PATH_MAX];
  if (getcwd(cwd, sizeof(cwd))) {
    std::cout << "\n=== Current Working Directory ===\n";
    std::cout << cwd << "\n";
  }
}

void print_open_fds() {
  std::cout << "\n=== Open File Descriptors ===\n";
  DIR *dir = opendir("/proc/self/fd");
  if (!dir) {
    std::cerr << "Failed to open /proc/self/fd\n";
    return;
  }

  struct dirent *entry;
  while ((entry = readdir(dir)) != nullptr) {
    if (entry->d_name[0] == '.')
      continue;
    std::string fd_path = std::string("/proc/self/fd/") + entry->d_name;
    char target[PATH_MAX];
    ssize_t len = readlink(fd_path.c_str(), target, sizeof(target) - 1);
    if (len != -1) {
      target[len] = '\0';
      std::cout << entry->d_name << " -> " << target << "\n";
    }
  }
  closedir(dir);
}

void print_env_vars() {
  extern char **environ;
  std::cout << "\n=== Environment Variables ===\n";
  for (char **env = environ; *env != 0; ++env) {
    std::cout << *env << "\n";
  }
}

int main() {
  print_basic_info();
  print_memory_info();
  print_cpu_info();
  print_limits_info();
  print_cwd();
  print_open_fds();
  print_env_vars();

  return 0;
}
