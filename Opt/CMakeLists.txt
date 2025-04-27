cmake_minimum_required(VERSION 3.16)
project(
  example
  VERSION 0.0.0
  DESCRIPTION "Common Library"
  HOMEPAGE_URL "https://github.com/laoheshanwuwukai/YuFeng"
  LANGUAGES CXX)

set(CMAKE_PREFIX_PATH "${CMAKE_PREFIX_PATH};/usr/local/lib/cmake/nlopt")
find_package(NLopt REQUIRED)

add_executable(nlexample nlopt/example.cc)
target_link_libraries(nlexample nlopt)
