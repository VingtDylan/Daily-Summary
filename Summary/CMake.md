CMakeLists.txt (templates)

```
# 声明要求的cmake的最低版本
cmake_minimum_required(VERSION 2.8)

# 设置编译模式
set(CMAKE_BUILD_TYPE "Debug" || "Release")

# 声明一个cmake工程
project(HelloWorld)

# 添加c++ 11标准支持
set(CMKAE_CXX_FLAGS "-std=c++11")

# 寻找opencv库并添加
find_package(OpenCV (4 REQUIRED))
include_directories(${OpenCV_INCLUDE_DIRS})
target_link_library(project ${OpenCV_LIBS})

# 添加一个cmake工程
# 语法: add_executable(程序名 源代码文件)
add_executable(HelloWorld HelloWorld.cpp)

# 共享库
add_library(HelloWorld_shared SHARED libHelloWorld.cpp)

# 链接共享库
add_executable(useHello useHello.cpp)
target_link_library(useHello HelloWorld_shared)

```

* cmake version:

  ```
  cmake -version
  ```

* 外加库

  ```
  find_package(OpenCV (4 REQUIRED))
  include_directories(${OpenCV_INCLUDE_DIRS})
  target_link_library(project ${Opencv_LIBS})
  ```

* c++ 11标准支持

  ```
  set(CMKAE_CXX_FLAGS "-std=c++11")
  ```

* 共享库

  ```
  add_library(HelloWorld_shared SHARED libHelloWorld.cpp)
  ```

* TODO