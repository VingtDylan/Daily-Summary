cmake_minimum_required(VERSION 3.16)

set(CMAKE_BUILD_TYPE "Release")

project(imageBasics)

set(CMAKE_CXX_FLAGS "-std=c++11")

find_package(OpenCV 4 REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(imageBasics main.cpp)
target_link_libraries(imageBasics ${OpenCV_LIBS})
