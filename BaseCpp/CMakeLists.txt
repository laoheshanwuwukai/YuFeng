cmake_minimum_required(VERSION 3.16)
project(
  common
  VERSION 0.1.2
  DESCRIPTION "Common Library"
  HOMEPAGE_URL "https://github.com/laoheshanwuwukai/YuFeng"
  LANGUAGES CXX)

if(PROJECT_BINARY_DIR STREQUAL PROJECT_SOURCE_DIR)
  message(
    FATAL_ERROR
      "In-Source build is not allowed , Please make a new directory(called a build directory) and run CMake from there"
  )
endif()

message(STATUS "project name ${PROJECT_NAME}")
message(STATUS "project version major ${PROJECT_VERSION_MAJOR}")
message(STATUS "project version minor ${PROJECT_VERSION_MINOR}")
message(STATUS "project version patch ${PROJECT_VERSION_PATCH}")
message(STATUS "project source dir ${PROJECT_SOURCE_DIR}")
message(STATUS "project binary dir ${PROJECT_BINARY_DIR}")

if(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  set(CMAKE_INSTALL_PREFIX
      ${CMAKE_SOURCE_DIR}/install
      CACHE PATH "Default install directory" FORCE)
endif()

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE RelWithDebInfo)
endif()

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_STANDARD 17)

file(GLOB_RECURSE SOURCES "*.cpp")
list(FILTER SOURCES EXCLUDE REGEX
     ".*/test/.*|.*_test.cc|tools/.*|.*example.*|python/.*|mainboard/.*")
add_library(${PROJECT_NAME} SHARED ${SOURCES})
