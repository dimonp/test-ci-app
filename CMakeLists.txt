# Specifies the minimum required version of CMake
cmake_minimum_required(VERSION 3.31)

# Sets the project name and enables C++
project(MyConsoleApp VERSION 1.0 LANGUAGES CXX)

# Set the C++ standard (optional, but recommended for modern C++)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(fmt CONFIG REQUIRED)
find_package(spdlog CONFIG REQUIRED)
find_package(CLI11 CONFIG REQUIRED)

# Add an executable target from the source file
add_executable(MyConsoleApp main.cpp)

target_link_libraries(MyConsoleApp PRIVATE fmt::fmt)
target_link_libraries(MyConsoleApp PRIVATE spdlog::spdlog)
target_link_libraries(MyConsoleApp PRIVATE CLI11::CLI11)

##########################INSTALL#############################
install(TARGETS MyConsoleApp RUNTIME DESTINATION bin)
if(WIN32)
  install(FILES $<TARGET_RUNTIME_DLLS:MyConsoleApp> DESTINATION bin)
endif()

# install(CODE [[
#     file(GET_RUNTIME_DEPENDENCIES
#         EXECUTABLES $<TARGET_FILE:MyConsoleApp>
#         RESOLVED_DEPENDENCIES_VAR _resolved
#         UNRESOLVED_DEPENDENCIES_VAR _unresolved

#         # Skip Windows system DLLs
#         PRE_EXCLUDE_REGEXES "^api-ms-.*" "^ext-ms-.*"
#         # Skip system libraries
#         POST_EXCLUDE_REGEXES "^/usr/lib/.*" "^/lib/.*" ".*WINDOWS[\\\\/]system32.*"
#     )
#     foreach(_file ${_resolved})
#         file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE SHARED_LIBRARY FILES "${_file}")
#     endforeach()
# ]])
if(CMAKE_SYSTEM_NAME STREQUAL "Windows")
  set(CPACK_GENERATOR "ZIP")
elseif(CMAKE_SYSTEM_NAME STREQUAL "Linux")
  set(CPACK_GENERATOR "TGZ")
endif()
include(CPack)

#########################TEST##############################


include(CTest)

if(BUILD_TESTING)
  enable_testing()

  find_package(Catch2 REQUIRED)
  add_executable(UnitTests test.cpp)
  target_link_libraries(UnitTests PRIVATE Catch2::Catch2WithMain)

  include(Catch)
  catch_discover_tests(UnitTests)
endif()

