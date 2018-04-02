## Setting up a new C++ project and typical CMakefiles

### Directory Structure
```
|
|- include
|- src
|- tests
```

### Top Level CMakeLists.txt
```sh
cmake_minimum_required(VERSION 2.8)
project (RtlChecker)

SET( CMAKE_CXX_FLAGS -std=c++11 )
include_directories("${PROJECT_SOURCE_DIR}/include")

add_subdirectory (src)
add_subdirectory (test)
```

### src/CMakeLists.txt
```sh
add_library(libName file1.cpp)
```

### tests/CMakelists.txt
```sh
link_directories (${PROJECT_BINARY_DIR}/lib) 
add_executable(exeName test1.cpp)
target_link_libraries (exeName libName)
```
