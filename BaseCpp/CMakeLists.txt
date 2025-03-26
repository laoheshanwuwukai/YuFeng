cmake_minimum_required(VERSION 3.16)
project(
  common
  VERSION 0.1.2
  DESCRIPTION "Common Library"
  HOMEPAGE_URL "https://github.com/laoheshanwuwukai/YuFeng"
  LANGUAGES CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS on)
set(CMAKE_CXX_STANDARD 17)

message(STATUS "project name ${PROJECT_NAME}")
message(STATUS "project version major ${PROJECT_VERSION_MAJOR}")
message(STATUS "project version minor ${PROJECT_VERSION_MINOR}")
message(STATUS "project version patch ${PROJECT_VERSION_PATCH}")
message(STATUS "project source dir ${PROJECT_SOURCE_DIR}")
message(STATUS "project binary dir ${PROJECT_BINARY_DIR}")

if(PROJECT_BINARY_DIR STREQUAL PROJECT_SOURCE_DIR)
  message(FATAL_ERROR
    "In-Source build is not allowed")
endif()

